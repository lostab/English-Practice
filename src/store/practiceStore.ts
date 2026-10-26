import { create } from 'zustand';
import { persist } from 'zustand/middleware';
import { QUESTIONS } from '../data/questions';
import type { PracticeMode, ExamType, SectionType, PracticeSession, Question } from '../types';

interface PracticeStore {
  session: PracticeSession | null;
  history: { date: string; mode: PracticeMode; exam: ExamType; correct: number; total: number }[];
  startPractice: (mode: PracticeMode, exam: ExamType, section: SectionType, count?: number) => void;
  selectAnswer: (questionIndex: number, optionIndex: number) => void;
  goTo: (index: number) => void;
  next: () => void;
  prev: () => void;
  finish: () => void;
  reset: () => void;
}

// 全真模考抽题计划：严格对齐真实考试的题型结构与题量
// TOEIC 阅读：Part5 词汇语法 30 题 + Part6 短文填空 16 题 + Part7 阅读理解 54 题 = 100 题
// 模拟考真实结构：
// TOEIC 阅读：Part5 句子填空 30 + Part6 短文填空 16 + Part7 阅读理解 54 = 100 题
// TOEIC 听力：Part2 应答题 25（题库仅覆盖 33 道 P2，按全量抽取）
// TOEFL 阅读：3 篇文章 × 约 10 题 = 30 题
// TOEFL 听力：2 个 section ≈ 28 题
const MOCK_PLAN: Record<string, Record<number, number>> = {
  'toeic:reading': { 5: 30, 6: 16, 7: 54 },
  'toeic:listening': { 2: 33 },
  'toefl:reading': { 1: 30 },
  'toefl:listening': { 2: 28 },
};

// 由抽题计划计算某组合的模考总题数（供首页徽章展示）
export function mockQuestionCount(exam: ExamType, section: SectionType): number {
  const plan = MOCK_PLAN[`${exam}:${section}`];
  if (!plan) return 0;
  return Object.values(plan).reduce((a, b) => a + b, 0);
}

// 按条件过滤题库（碎片练习随机取1道流式刷题；模拟练习按真实考试结构抽题）
function pickQuestions(mode: PracticeMode, exam: ExamType, section: SectionType, count = 5) {
  const pool = QUESTIONS.filter(q => q.exam === exam && q.section === section);
  if (mode === 'mock') {
    const plan = MOCK_PLAN[`${exam}:${section}`];
    if (plan) {
      // 按真实考试结构：逐 part 随机抽取指定数量，不足则取该 part 全部
      const picked: typeof pool = [];
      for (const [part, need] of Object.entries(plan)) {
        const partQs = pool.filter(q => q.part === Number(part));
        const shuffled = [...partQs].sort(() => Math.random() - 0.5);
        picked.push(...shuffled.slice(0, Math.min(need, shuffled.length)));
      }
      return picked.length > 0 ? picked : pool.slice(0, 10);
    }
    // 无计划的组合：随机取 count 道兜底
    const shuffled = [...pool].sort(() => Math.random() - 0.5);
    return shuffled.slice(0, Math.min(count, shuffled.length));
  }
  // 碎片练习：随机取 count 道（默认1道，单题流）
  const shuffled = [...pool].sort(() => Math.random() - 0.5);
  return shuffled.slice(0, Math.min(count, shuffled.length));
}

// 碎片单题流：从未用过的题里抽一道新题
function pickNextQuestion(exam: ExamType, section: SectionType, usedIds: Set<string>): Question | null {
  const pool = QUESTIONS.filter(q => q.exam === exam && q.section === section && !usedIds.has(q.id));
  if (pool.length === 0) return null;
  return pool[Math.floor(Math.random() * pool.length)];
}

export const usePracticeStore = create<PracticeStore>()(
  persist(
    (set, get) => ({
      session: null,
      history: [],

      startPractice: (mode, exam, section, count = 5) => {
        const questions = pickQuestions(mode, exam, section, count);
        set({
          session: {
            mode,
            exam,
            section,
            questions,
            answers: new Array(questions.length).fill(null),
            currentIndex: 0,
            startTime: Date.now(),
            isFinished: false,
            stats: mode === 'fragment' ? { answered: 0, correct: 0 } : undefined,
          },
        });
      },

      selectAnswer: (questionIndex, optionIndex) => {
        const { session } = get();
        if (!session || session.isFinished) return;
        // 碎片模式：已答过不可改；模考模式：允许随时修改答案
        if (session.mode === 'fragment' && session.answers[questionIndex] !== null) return;
        
        const answers = [...session.answers];
        answers[questionIndex] = optionIndex;

        // 碎片单题流：累计统计 + 定格本题用时（刷新后恢复）
        const stats = session.stats;
        const elapsedSeconds =
          session.mode === 'fragment'
            ? Math.round((Date.now() - session.startTime) / 1000)
            : session.elapsedSeconds;
        if (stats && session.mode === 'fragment') {
          stats.answered += 1;
          if (optionIndex === session.questions[questionIndex].answer) stats.correct += 1;
        }

        set({ session: { ...session, answers, stats, elapsedSeconds } });
      },

      goTo: (index) => {
        const { session } = get();
        if (!session) return;
        const clamped = Math.max(0, Math.min(session.questions.length - 1, index));
        set({ session: { ...session, currentIndex: clamped } });
      },

      next: () => {
        const { session } = get();
        if (!session) return;

        if (session.mode === 'fragment') {
          // 单题流：抽下一道新题，保持单题 session
          const usedIds = new Set(session.questions.map(q => q.id));
          const nextQ = pickNextQuestion(session.exam, session.section, usedIds);
          if (nextQ) {
            set({
              session: {
                ...session,
                questions: [nextQ],
                answers: [null],
                currentIndex: 0,
                startTime: Date.now(), // 切换新题时重置计时
                elapsedSeconds: 0, // 新题重新计时
                stats: session.stats,
                isFinished: false,
              },
            });
          } else {
            // 题库刷完了，结束
            get().finish();
          }
          return;
        }

        if (session.currentIndex < session.questions.length - 1) {
          set({ session: { ...session, currentIndex: session.currentIndex + 1 } });
        } else if (session.mode === 'mock') {
          // 最后一题点"下一题"不自动交卷（交卷由"提交交卷"按钮控制）
          return;
        }
      },

      prev: () => {
        const { session } = get();
        if (!session) return;
        if (session.currentIndex > 0) {
          set({ session: { ...session, currentIndex: session.currentIndex - 1 } });
        }
      },

      finish: () => {
        const { session, history } = get();
        if (!session || session.isFinished) return;
        const totalSec = Math.round((Date.now() - session.startTime) / 1000);
        const finished: PracticeSession = {
          ...session,
          isFinished: true,
          elapsedSeconds: totalSec,
          // 核心：把 startTime 重置为“基于已用时倒推的固定时间戳”，彻底冻结实时计算差值
          startTime: Date.now() - totalSec * 1000,
        };
        // 碎片模式：统计用累计 stats
        let correct: number;
        if (session.mode === 'fragment' && session.stats) {
          correct = session.stats.correct;
        } else {
          correct = finished.answers.filter((a, i) => a === finished.questions[i].answer).length;
        }
        set({
          session: finished,
          history: [
            {
              date: new Date().toISOString().slice(0, 10),
              mode: session.mode,
              exam: session.exam,
              correct,
              total: session.stats ? session.stats.answered : session.questions.length,
            },
            ...history,
          ],
        });
      },

      reset: () => set({ session: null }),
    }),
    {
      name: 'testprep-practice-storage', // key in localStorage
      partialize: (state) => ({ session: state.session }), // only persist session data
    }
  ),
);