import { useEffect, useRef, useState } from 'react';
import { usePracticeStore, mockQuestionCount } from './store/practiceStore';
import type { PracticeSession } from './types';
import { QUESTIONS } from './data/questions';
import type { Question } from './data/questions';

// ============ 全屏触发（仅移动端：点击任意地方进入全屏；PC 端不触发） ============
function requestFullscreen() {
  // 仅移动端生效：触屏设备（粗指针）或窄屏。PC 桌面鼠标/键盘直接忽略
  const isMobile =
    window.matchMedia('(pointer: coarse)').matches ||
    window.matchMedia('(max-width: 768px)').matches ||
    'ontouchstart' in window;
  if (!isMobile) return;
  if (!document.fullscreenElement) {
    document.documentElement.requestFullscreen().catch(() => {});
  }
}

// 计算托业/托福真实折算分
function calculateScore(exam: ExamType, section: SectionType, correct: number, total: number): { score: number; maxScore: number; level: string } {
  if (total === 0) return { score: 0, maxScore: exam === 'toeic' ? 495 : 30, level: '未作答' };
  const ratio = correct / total;
  if (exam === 'toeic') {
    // TOEIC 听力或阅读单项满分 495
    const score = Math.round(100 + ratio * 395);
    let level = '需夯实基础';
    if (score >= 450) level = '金牌满分实力';
    else if (score >= 400) level = '优秀高分水平';
    else if (score >= 320) level = '良好中等水平';
    return { score, maxScore: 495, level };
  } else {
    // TOEFL 单项满分 30
    const score = Math.round(ratio * 30);
    let level = '需夯实基础';
    if (score >= 26) level = '母语/顶尖水平';
    else if (score >= 22) level = '优秀高分水平';
    else if (score >= 17) level = '良好中等水平';
    return { score, maxScore: 30, level };
  }
}
function ResultCard({ session }: { session: PracticeSession }) {
  const { reset } = usePracticeStore();
  // 展开中的错题 id（可折叠复盘）
  const [expandedId, setExpandedId] = useState<string | null>(null);
  // 碎片单题流用累计 stats；模考模式用 answers
  const total = session.stats ? session.stats.answered : session.questions.length;
  const correct = session.stats
    ? session.stats.correct
    : session.answers.filter((a, i) => a === session.questions[i].answer).length;
  const wrong = Math.max(0, total - correct);
  const accuracy = total > 0 ? Math.round((correct / total) * 100) : 0;
  // 总用时：挂载时计算一次并冻结（useState 惰性初始化），重渲染/展开错题/刷新恢复都不会再变
  const [timeUsedSec] = useState(() =>
    session.elapsedSeconds !== undefined
      ? session.elapsedSeconds
      : Math.max(0, Math.round((Date.now() - session.startTime) / 1000))
  );
  const wrongQuestions = session.stats
    ? []
    : session.questions.filter((q, i) => session.answers[i] !== q.answer);

  // 模考模式计算真实考试折算分（TOEIC 单项 495 / TOEFL 单项 30）；碎片模式不适用
  const isMock = !session.stats;
  const scoreInfo = isMock
    ? calculateScore(session.exam, session.section, correct, total)
    : null;

  return (
    <div onClick={requestFullscreen} className="app-viewport bg-slate-950 text-slate-100 flex flex-col">
      {/* 成绩单头部（固定区域：标题 + 极简分数大卡 + 四合一统计卡） */}
      <div className="bg-slate-900/90 backdrop-blur-xl border-b border-slate-800 shadow-2xl relative overflow-hidden shrink-0 pt-safe">
        <div className="absolute top-0 left-0 right-0 h-1 bg-gradient-to-r from-indigo-500 via-amber-400 to-emerald-400"></div>
        <div className="max-w-2xl lg:max-w-6xl mx-auto px-4 sm:px-6 py-2.5">
          {/* 极简标题行 */}
          <div className="flex items-center justify-between gap-4 mb-2">
            <div className="flex items-center gap-2">
              <span className="text-base">🏆</span>
              <h2 className="text-sm font-bold tracking-tight text-white">
                {isMock ? '模考成绩单' : '碎片练习小结'}
              </h2>
              <span className="text-[11px] text-slate-400">
                ({session.exam === 'toeic' ? 'TOEIC' : 'TOEFL'} · {session.section === 'listening' ? '听力' : '阅读'})
              </span>
            </div>
            <span className={`px-2.5 py-0.5 rounded-full text-[11px] font-bold ${
              scoreInfo
                ? scoreInfo.score >= (session.exam === 'toeic' ? 400 : 22)
                  ? 'bg-emerald-500/15 border border-emerald-500/30 text-emerald-300'
                  : scoreInfo.score >= (session.exam === 'toeic' ? 320 : 17)
                    ? 'bg-amber-500/15 border border-amber-500/30 text-amber-300'
                    : 'bg-rose-500/15 border border-rose-500/30 text-rose-300'
                : 'bg-slate-800 border border-slate-700 text-slate-300'
            }`}>
              {scoreInfo ? scoreInfo.level : (session.stats ? `${correct}/${total} 答对` : '练习完成')}
            </span>
          </div>

          {/* 极简分数卡片（居中显示） */}
          {scoreInfo && (
            <div className="mb-2 bg-gradient-to-r from-indigo-500/15 via-purple-500/10 to-slate-900/40 border border-indigo-500/30 rounded-xl px-6 py-3 flex flex-col items-center justify-center gap-1">
              <span className="text-[11px] font-bold uppercase tracking-widest text-indigo-300">本次模考得分</span>
              <div className="flex items-baseline gap-1.5">
                <span className="text-3xl font-black text-white">{scoreInfo.score}</span>
                <span className="text-sm font-bold text-slate-400">/ {scoreInfo.maxScore}</span>
              </div>
            </div>
          )}

          {/* 极扁平统计卡片（4卡并排） */}
          <div className="grid grid-cols-4 gap-2">
            <div className="bg-slate-800/60 rounded-lg px-2 py-1.5 border border-slate-700/50 text-center flex items-center justify-between">
              <span className="text-[10px] text-slate-400">正确</span>
              <span className="text-sm font-black text-indigo-400">{correct}</span>
            </div>
            <div className="bg-slate-800/60 rounded-lg px-2 py-1.5 border border-slate-700/50 text-center flex items-center justify-between">
              <span className="text-[10px] text-slate-400">错误</span>
              <span className="text-sm font-black text-rose-400">{wrong}</span>
            </div>
            <div className="bg-slate-800/60 rounded-lg px-2 py-1.5 border border-slate-700/50 text-center flex items-center justify-between">
              <span className="text-[10px] text-slate-400">正确率</span>
              <span className="text-sm font-black text-emerald-400">{accuracy}%</span>
            </div>
            <div className="bg-slate-800/60 rounded-lg px-2 py-1.5 border border-slate-700/50 text-center flex items-center justify-between">
              <span className="text-[10px] text-slate-400">总用时</span>
              <span className="text-sm font-black text-amber-400">{timeUsedSec}s</span>
            </div>
          </div>
        </div>
      </div>

      {/* 错题复盘标题（固定） */}
      {wrongQuestions.length > 0 && (
        <div className="shrink-0 bg-slate-950/90 backdrop-blur-xl border-b border-slate-800/80 px-4 sm:px-6 py-2.5">
          <div className="max-w-2xl lg:max-w-6xl mx-auto flex items-center justify-between">
            <h3 className="text-xs font-bold text-white flex items-center gap-2">
              <span className="w-1.5 h-1.5 bg-rose-500 rounded-full"></span>
              错题复盘与深度解析
              <span className="text-[10px] bg-slate-800 text-rose-300 px-1.5 py-0.2 rounded-full border border-rose-500/30 font-bold">
                {wrongQuestions.length} 题
              </span>
            </h3>
            <span className="text-[10px] text-slate-400">点击展开详情</span>
          </div>
        </div>
      )}

      {/* 错题回顾 (去掉了外层大卡片包裹，全宽平铺滚动) */}
      <div className="flex-1 min-h-0 overflow-y-auto px-4 sm:px-6 py-3">
        <div className="max-w-2xl lg:max-w-6xl mx-auto">
          {wrongQuestions.length > 0 ? (
            <div className="space-y-2.5">
                {wrongQuestions.map((q, idx) => {
                  const userAns = session.answers[session.questions.indexOf(q)];
                  const isOpen = expandedId === q.id;
                  return (
                    <div key={q.id} className="bg-slate-800/50 rounded-2xl border border-slate-700/50 overflow-hidden">
                      {/* 可点击头部（始终显示题目摘要） */}
                      <button
                        onClick={() => setExpandedId(isOpen ? null : q.id)}
                        className="w-full flex items-center justify-between gap-3 p-4 text-left hover:bg-slate-800/80 transition-colors"
                      >
                        <div className="min-w-0">
                          <div className="text-xs font-bold text-rose-400 mb-1">❌ 错题 #{idx + 1}</div>
                          <div className="font-medium text-slate-200 text-sm line-clamp-2">{q.question}</div>
                        </div>
                        <span className={`text-slate-500 text-xs shrink-0 transition-transform ${isOpen ? 'rotate-180' : ''}`}>
                          ▼
                        </span>
                      </button>

                      {/* 展开内容：正确/你的答案 + 解析 */}
                      {isOpen && (
                        <div className="px-4 pb-4 space-y-2.5 animate-fadeIn">
                          <div className="grid grid-cols-1 sm:grid-cols-2 gap-2 text-xs">
                            <div className="bg-emerald-500/10 border border-emerald-500/20 text-emerald-300 p-2.5 rounded-xl font-medium">
                              ✓ 正确：{q.options[q.answer]}
                            </div>
                            <div className="bg-rose-500/10 border border-rose-500/20 text-rose-300 p-2.5 rounded-xl font-medium">
                              ✗ 你的：{userAns !== null ? q.options[userAns] : '未作答'}
                            </div>
                          </div>
                          <div className="text-xs text-slate-400 bg-slate-900/60 p-3 rounded-xl border border-slate-700/50 leading-relaxed">
                            <strong className="text-slate-200">💡 解析：</strong>{q.explanation}
                          </div>
                        </div>
                      )}
                    </div>
                  );
                })}
            </div>
          ) : session.stats ? (
            <div className="bg-slate-900/80 backdrop-blur-xl border border-slate-800 rounded-3xl p-8 shadow-2xl text-center">
              <div className="text-2xl mb-3">📊</div>
              <div className="text-slate-300 font-semibold mb-1">
                本组碎片练习 {session.stats.answered} 题，答对 {session.stats.correct} 题
              </div>
              <div className="text-slate-500 text-xs">
                正确率 {session.stats.answered > 0 ? Math.round((session.stats.correct / session.stats.answered) * 100) : 0}% · 用时 {timeUsedSec}s
              </div>
            </div>
          ) : (
            <div className="bg-slate-900/80 backdrop-blur-xl border border-slate-800 rounded-3xl p-8 shadow-2xl text-center">
              <div className="text-3xl mb-3">🎉</div>
              <div className="text-slate-300 font-semibold">全部答对，没有任何错题！</div>
            </div>
          )}
        </div>
      </div>

      {/* 底部按钮 */}
      <div className="border-t border-slate-800 bg-slate-900/80 backdrop-blur-xl shrink-0 px-6 py-3">
        <div className="max-w-2xl lg:max-w-6xl mx-auto text-center">
          <button
            onClick={reset}
            className="px-8 py-2.5 bg-gradient-to-r from-indigo-500 to-purple-600 hover:from-indigo-600 hover:to-purple-700 text-white font-bold rounded-2xl shadow-lg shadow-indigo-500/25 transition-all transform active:scale-95"
          >
            返回首页，开启新练习
          </button>
        </div>
      </div>
    </div>
  );
}

// ============ 听力播放器（原生 HTML5 音频，100% 可靠） ============
function AudioPlayer({ text, audioSrc }: { text: string; audioSrc?: string }) {
  const audioRef = useRef<HTMLAudioElement | null>(null);
  const [isPlaying, setIsPlaying] = useState(false);
  const [progress, setProgress] = useState(0);
  const [currentTime, setCurrentTime] = useState(0);
  const [duration, setDuration] = useState(0);

  // audioSrc 变化时强制重置播放器（防止旧音频残留）
  useEffect(() => {
    setIsPlaying(false);
    setProgress(0);
    setCurrentTime(0);
    setDuration(0);
    const audio = audioRef.current;
    if (audio) {
      audio.pause();
      audio.currentTime = 0;
    }
  }, [audioSrc]);

  // 原生 audio 播放
  const togglePlay = () => {
    const audio = audioRef.current;
    if (!audio) return;
    if (audio.paused) {
      audio.play().catch(err => {
        console.error('[AudioPlayer] play failed:', err);
        alert('音频播放失败：' + err.message);
      });
    } else {
      audio.pause();
    }
  };

  const onTimeUpdate = () => {
    const audio = audioRef.current;
    if (audio && audio.duration) {
      setCurrentTime(audio.currentTime);
      setDuration(audio.duration);
      setProgress((audio.currentTime / audio.duration) * 100);
    }
  };

  const onEnded = () => {
    setIsPlaying(false);
    setProgress(100);
    setCurrentTime(duration);
  };

  return (
    <div className="bg-indigo-950/60 border border-indigo-700/40 rounded-2xl p-3 mb-3 w-full">
      <div className="flex flex-wrap items-center justify-between gap-2 mb-2">
        <div className="flex items-center gap-2">
          <span className="inline-flex w-7 h-7 items-center justify-center rounded-lg bg-indigo-500/20 border border-indigo-500/30 text-indigo-300 text-xs">
            🎧
          </span>
          <span className="text-[11px] font-bold text-indigo-300 uppercase tracking-wider">听力录音</span>
          {/* 秒数标签：固定宽度始终占位（duration 未加载时 invisible），避免播放按钮闪跳 */}
          <span className={`text-[10px] text-indigo-400/80 tabular-nums hidden sm:inline w-16 text-right ${duration > 0 ? '' : 'invisible'}`}>
            {duration > 0 ? `${Math.floor(currentTime)}s / ${Math.floor(duration)}s` : '0s / 0s'}
          </span>
        </div>

        <div className="flex items-center gap-2">
          <button
            onClick={togglePlay}
            className={`inline-flex items-center gap-1.5 px-3 py-1.5 rounded-lg text-xs font-bold transition-all shadow-lg ${
              isPlaying
                ? 'bg-rose-500 hover:bg-rose-600 text-white shadow-rose-500/25'
                : 'bg-indigo-600 hover:bg-indigo-500 text-white shadow-indigo-500/25'
            }`}
          >
            {isPlaying ? '⏸ 暂停' : '▶ 播放'}
          </button>
        </div>
      </div>

      <details className="group">
        <summary className="cursor-pointer text-[10px] text-indigo-300/70 hover:text-indigo-200 font-medium select-none">
          📄 查看听力原文（答题后再对照）
        </summary>
        <p className="mt-1.5 text-[11px] text-indigo-200/80 leading-relaxed bg-slate-900/40 rounded-lg p-2 border border-slate-700/40 max-h-24 overflow-y-auto">
          {text}
        </p>
      </details>

      {/* 原生 audio 元素 */}
      {audioSrc && (
        <audio
          ref={audioRef}
          src={audioSrc}
          preload="auto"
          onPlay={() => setIsPlaying(true)}
          onPause={() => setIsPlaying(false)}
          onEnded={onEnded}
          onTimeUpdate={onTimeUpdate}
          onLoadedMetadata={onTimeUpdate}
        />
      )}
    </div>
  );
}

// ============ 题目卡片（精致拟真 APP 风格） ============
function QuestionCard({
  question,
  questionIndex,
  selected,
  onSelect,
  showAnswer,
}: {
  question: Question;
  questionIndex: number;
  selected: number | null;
  onSelect: (idx: number) => void;
  showAnswer: boolean;
}) {
  const isCorrect = selected === question.answer;

  return (
    <div className="bg-slate-900/90 backdrop-blur-xl border border-slate-800 rounded-3xl p-4 sm:p-6 shadow-2xl text-slate-100 h-full flex flex-col overflow-hidden">
      <div className="flex justify-between items-center mb-4">
        <span className="px-3 py-1 bg-indigo-500/15 border border-indigo-500/30 text-indigo-300 rounded-full text-[11px] font-bold tracking-wider uppercase">
          Question {questionIndex + 1}
        </span>
        <span className="px-3 py-1 bg-slate-800/80 border border-slate-700 text-slate-400 rounded-full text-[11px] font-semibold tracking-widest uppercase">
          {question.exam} · Part {question.part}
        </span>
      </div>

      <div className={
        question.passage
          ? "flex-1 min-h-0 grid grid-cols-1 grid-rows-[1fr_auto_1fr] gap-3 lg:grid-cols-[5fr_6fr] lg:grid-rows-[auto_minmax(0,1fr)] lg:gap-x-6 lg:gap-y-3"
          : "flex-1 min-h-0 flex flex-col"
      }>
        {/* 左栏/阅读材料：移动端第1行(1fr)与选项等高；PC 端左列跨两行 */}
        {question.passage && (
          <div className="flex flex-col min-h-0 lg:col-start-1 lg:row-start-1 lg:row-span-2">
            <div className="bg-slate-800/60 border border-slate-700/50 rounded-2xl p-3 text-[13px] text-slate-300 leading-relaxed flex-1 min-h-0 overflow-y-auto">
              <div className="text-[11px] font-bold text-slate-400 uppercase tracking-wider mb-1">📖 阅读材料</div>
              {question.passage}
            </div>
            {question.audio && (
              <div className="mt-2">
                <AudioPlayer text={question.audio} audioSrc={`/audio/${question.id}.wav?v=3`} />
              </div>
            )}
          </div>
        )}

        {/* 无阅读材料时：音频播放器直接放题目上方 */}
        {!question.passage && question.audio && (
          <div className="mb-3 flex justify-center">
            <AudioPlayer text={question.audio} audioSrc={`/audio/${question.id}.wav?v=3`} />
          </div>
        )}

        {/* 题干：移动端第2行(auto)；PC 端右列第1行(auto，紧贴顶部) */}
        <h3 className="text-base sm:text-lg font-bold text-white leading-snug shrink-0 lg:col-start-2 lg:row-start-1">
          {question.question}
        </h3>

        {/* 选项列表：移动端第3行(1fr 与材料等高)；PC 端右列第2行(1fr 撑满剩余) */}
        <div className="space-y-2.5 flex flex-col min-h-0 overflow-y-auto lg:col-start-2 lg:row-start-2">
          {question.options.map((opt, i) => {
            let style = 'border-slate-800 bg-slate-800/40 hover:bg-slate-700/50 text-slate-200';
            if (selected === i) {
              style = showAnswer
                ? (isCorrect ? 'border-emerald-500 bg-emerald-500/15 text-emerald-200 shadow-lg shadow-emerald-500/10' : 'border-rose-500 bg-rose-500/15 text-rose-200 shadow-lg shadow-rose-500/10')
                : 'border-indigo-500 bg-indigo-500/20 text-indigo-200 ring-2 ring-indigo-500/30 shadow-lg';
            } else if (showAnswer && i === question.answer) {
              style = 'border-emerald-500 bg-emerald-500/15 text-emerald-200 shadow-lg shadow-emerald-500/10';
            }

            return (
              <button
                key={i}
                onClick={() => onSelect(i)}
                disabled={showAnswer}
                className={`w-full text-left border-2 rounded-xl p-3 text-[13px] font-semibold transition-all flex items-center gap-3 ${style}`}
              >
                <span className={`w-8 h-8 rounded-lg flex items-center justify-center font-bold text-xs shrink-0 ${
                  selected === i ? 'bg-indigo-500 text-white shadow-md' : 'bg-slate-800 text-slate-400 border border-slate-700'
                }`}>
                  {String.fromCharCode(65 + i)}
                </span>
                <span className="flex-1 leading-normal">{opt}</span>
              </button>
            );
          })}
        </div>{/* 选项列表容器 */}
      </div>{/* 有材料:移动1fr-auto-1fr三行/PC两栏；无材料:单栏 */}
      {showAnswer && (
        <div className={`mt-4 p-4 rounded-2xl border text-[13px] leading-relaxed animate-fadeIn ${
          isCorrect
            ? 'bg-emerald-500/10 border-emerald-500/30 text-emerald-200'
            : 'bg-rose-500/10 border-rose-500/30 text-rose-200'
        }`}>
          <div className={`font-bold mb-1.5 flex items-center gap-2 ${
            isCorrect ? 'text-emerald-300' : 'text-rose-300'
          }`}>
            {isCorrect ? '✅ 回答正确！' : '❌ 回答错误'}
            {!isCorrect && selected !== null && (
              <span className="text-xs font-semibold opacity-80">
                你的选择：{question.options[selected]}
              </span>
            )}
          </div>
          <div className="text-slate-300">
            <span className="font-bold text-white">💡 专家名师解析：</span>
            {question.explanation}
          </div>
        </div>
      )}
    </div>
  );
}

// ============ 练习主界面 ===========
function PracticeView({ session }: { session: PracticeSession }) {
  const { selectAnswer, next, prev, finish, reset } = usePracticeStore();
  const current = session.questions[session.currentIndex];
  const isFragment = session.mode === 'fragment';
  const answeredCount = session.answers.filter(a => a !== null).length;

  // 刷新后如果当前题已经答过，自动恢复解析显示状态（碎片模式或模考已查看解析状态）
  const [showAnswer, setShowAnswer] = useState(
    isFragment ? session.answers[session.currentIndex] !== null : false
  );
  const [elapsed, setElapsed] = useState(0);

  const hasAnsweredCurrent = session.answers[session.currentIndex] !== null;

  // 切换题目或新题初始化时重置本地计时（仅碎片模式；模考持续计时不重置）
  useEffect(() => {
    if (!isFragment) return;
    if (session.elapsedSeconds !== undefined && session.elapsedSeconds > 0) {
      setElapsed(session.elapsedSeconds);
    } else {
      setElapsed(0);
    }
  }, [current.id, session.elapsedSeconds, isFragment]);

  useEffect(() => {
    // 恢复已过去的用时（组件刷新后从 session 恢复）
    if (session.elapsedSeconds !== undefined && session.elapsedSeconds > 0) {
      setElapsed(session.elapsedSeconds);
      return;
    }
    // 碎片模式：选完答案后暂停计时（每题单独计时）；模考：持续计时（只记总时间）
    if (isFragment && hasAnsweredCurrent) return;
    const timer = setInterval(() => setElapsed(Math.round((Date.now() - session.startTime) / 1000)), 1000);
    return () => clearInterval(timer);
  }, [session.startTime, hasAnsweredCurrent, isFragment, session.elapsedSeconds]);

  useEffect(() => {
    // 模考模式不再自动交卷：必须由用户主动点击“提交交卷”才出结果
    // （保留此函数仅为兼容，实际交卷走按钮 onClick → finish()）
  }, [isFragment]);

  return (
    <div onClick={requestFullscreen} className="app-viewport bg-slate-950 text-slate-100 flex flex-col">
      {/* 顶栏 */}
      <div className="bg-slate-900/90 backdrop-blur-xl border-b border-slate-800 z-25 shrink-0 flex items-center">
        <div className="max-w-2xl lg:max-w-6xl mx-auto px-4 py-3 w-full flex justify-between items-center text-xs">
          <div className="flex items-center gap-2">
            <span className="px-2.5 py-1 bg-indigo-500/10 border border-indigo-500/20 text-indigo-300 rounded-lg font-bold text-[10px] leading-none flex items-center">
              {session.mode === 'fragment' ? '⚡ 碎片' : '📝 模考'}
            </span>
            <span className="font-black text-slate-300 text-[9px] px-1.5 py-1 rounded bg-slate-800/90 border border-slate-700/60 tracking-wider leading-none flex items-center">
              {session.exam === 'toeic' ? 'TOEIC' : 'TOEFL'}
            </span>
          </div>
          <div className="flex items-center gap-2.5 text-slate-300 text-xs font-bold">
            {isFragment ? (
              <span className="bg-slate-800/80 px-2.5 py-1 rounded-lg border border-slate-700/60 leading-none flex items-center">⏱ {elapsed}s</span>
            ) : (
              <>
                <span className="bg-slate-800/80 px-2.5 py-1 rounded-lg border border-slate-700/60 leading-none flex items-center">⏱ {elapsed}s</span>
                <span className="text-indigo-400 font-bold bg-indigo-500/10 px-2.5 py-1 rounded-lg border border-indigo-500/20 leading-none flex items-center">{answeredCount}/{session.questions.length}</span>
              </>
            )}
          </div>
        </div>
      </div>

      {/* 题目区（不整体滚动，内部由 QuestionCard 自行分割滚动） */}
      <div className="flex-1 min-h-0 overflow-hidden px-4 sm:px-6 py-4">
        <div className="max-w-2xl lg:max-w-6xl mx-auto h-full">
          <QuestionCard
            key={current.id}
            question={current}
            questionIndex={session.currentIndex}
            selected={session.answers[session.currentIndex]}
            onSelect={(i) => { selectAnswer(session.currentIndex, i); setShowAnswer(isFragment); }}
            showAnswer={showAnswer}
          />
        </div>
      </div>

      {/* 底部导航栏 */}
      <div className="bg-slate-900/90 backdrop-blur-xl border-t border-slate-800 pt-2.5 pb-5 px-4 sm:px-6 pb-safe z-20 shadow-2xl shrink-0">
        <div className="max-w-2xl lg:max-w-6xl mx-auto grid grid-cols-3 items-center gap-3">
          {/* 左列：上一题（碎片模式无） */}
          <div className="flex justify-start">
            {!isFragment && (
              <button
                onClick={prev}
                disabled={session.currentIndex === 0}
                className="px-4 py-2 rounded-lg border border-slate-700 bg-slate-800 text-slate-300 font-semibold text-xs disabled:opacity-30 hover:bg-slate-700 transition-all"
              >
                ← 上一题
              </button>
            )}
          </div>

          {/* 中列：退出练习（始终居中） */}
          <div className="flex justify-center">
            <button
              onClick={reset}
              className="px-4 py-2 rounded-lg border border-slate-700/60 bg-slate-800/60 text-slate-400 hover:text-slate-300 hover:bg-slate-700/60 font-semibold text-xs transition-all active:scale-95"
            >
              退出练习
            </button>
          </div>

          {/* 右列：碎片=下一题；模考=最后一题显示提交交卷（手工交卷，可先修改答案） */}
          <div className="flex justify-end">
            <button
              onClick={() => {
                setShowAnswer(false);
                if (isFragment) next();
                else if (session.currentIndex === session.questions.length - 1) finish();
                else next();
              }}
              className="px-5 py-2 rounded-lg bg-indigo-600 hover:bg-indigo-500 text-white font-bold text-xs shadow-lg shadow-indigo-500/25 transition-all active:scale-95"
            >
              {isFragment ? '下一题 →' : (session.currentIndex === session.questions.length - 1 ? '交卷' : '下一题 →')}
            </button>
          </div>
        </div>
      </div>
    </div>
  );
}

// ============ 首页（高颜值现代化 Dashboard） ============
export default function App() {
  const session = usePracticeStore(s => s.session);
  const [selectedExam, setSelectedExam] = useState<'toeic' | 'toefl'>('toeic');
  const [selectedSection, setSelectedSection] = useState<'listening' | 'reading'>('reading');

  if (session) {
    return session.isFinished ? <ResultCard session={session} /> : <PracticeView session={session} />;
  }

  return (
    <div onClick={requestFullscreen} className="app-viewport bg-slate-950 text-slate-100 flex flex-col items-center justify-center p-4 sm:p-6 relative overflow-hidden cursor-pointer md:cursor-default">
      {/* 背景装饰光晕 */}
      <div className="absolute top-1/4 left-1/2 -translate-x-1/2 -translate-y-1/2 w-96 h-96 bg-indigo-600/15 rounded-full blur-3xl pointer-events-none"></div>
      <div className="absolute bottom-1/4 right-1/4 w-80 h-80 bg-purple-600/15 rounded-full blur-3xl pointer-events-none"></div>

      {/* 桌面端：横向双栏 */}
      <div className="w-full max-w-md lg:max-w-6xl z-10 flex flex-col lg:flex-row lg:items-center gap-8">
        {/* 左栏：标题 + 统计 */}
        <div className="text-center lg:text-center lg:flex-1">
          <div className="inline-flex items-center gap-2 px-4 py-1.5 rounded-full bg-gradient-to-r from-indigo-500/10 to-purple-500/10 border border-indigo-500/30 text-indigo-300 text-xs font-bold mb-5 tracking-wide shadow-sm">
            🔥 真题突击
          </div>
          <h1 className="text-4xl sm:text-5xl xl:text-6xl font-black tracking-tight mb-3 text-white">
            TOEIC & TOEFL <br/>
            <span className="text-transparent bg-clip-text bg-gradient-to-r from-indigo-400 via-purple-300 to-amber-300">
              高分直通车
            </span>
          </h1>
          <p className="text-slate-400 text-sm sm:text-base mb-6">
            碎片微练 ∙ 全真模考 ∙ 权威解析，随时随地高效备考。
          </p>

          {/* 统计卡片（仅桌面显示，动态统计） */}
          <div className="hidden lg:grid grid-cols-4 gap-3">
            <div className="bg-slate-900/60 border border-slate-800 rounded-2xl p-3 text-center">
              <div className="text-xl font-black text-indigo-400">{QUESTIONS.length}</div>
              <div className="text-[10px] text-slate-500 font-semibold uppercase mt-0.5">总题库</div>
            </div>
            <div className="bg-slate-900/60 border border-slate-800 rounded-2xl p-3 text-center">
              <div className="text-xl font-black text-amber-400">2</div>
              <div className="text-[10px] text-slate-500 font-semibold uppercase mt-0.5">考试科目</div>
            </div>
            <div className="bg-slate-900/60 border border-slate-800 rounded-2xl p-3 text-center">
              <div className="text-xl font-black text-emerald-400">{QUESTIONS.filter(q => q.section === 'listening').length}</div>
              <div className="text-[10px] text-slate-500 font-semibold uppercase mt-0.5">听力题</div>
            </div>
            <div className="bg-slate-900/60 border border-slate-800 rounded-2xl p-3 text-center">
              <div className="text-xl font-black text-rose-400">{QUESTIONS.filter(q => q.section === 'reading').length}</div>
              <div className="text-[10px] text-slate-500 font-semibold uppercase mt-0.5">阅读题</div>
            </div>
          </div>
        </div>

        {/* 右栏：选择面板 */}
        <div className="w-full lg:w-[440px] xl:w-[480px] bg-slate-900/80 backdrop-blur-2xl border border-slate-800 rounded-3xl shadow-2xl p-5 sm:p-6">
          {/* 1. 考试选择 */}
          <div className="mb-4">
            <label className="block text-[11px] font-bold uppercase tracking-widest text-slate-400 mb-2">
              1. 选择考试项目
            </label>
            <div className="grid grid-cols-2 gap-2.5">
              <button
                onClick={() => setSelectedExam('toeic')}
                className={`py-3 px-3.5 rounded-2xl border-2 font-bold text-sm transition-all flex items-center justify-center gap-2 ${
                  selectedExam === 'toeic'
                    ? 'border-amber-400 bg-amber-500/10 text-amber-300 shadow-lg shadow-amber-500/10'
                    : 'border-slate-800 bg-slate-800/40 text-slate-400 hover:bg-slate-800'
                }`}
              >
                🏢 TOEIC 托业
              </button>
              <button
                onClick={() => setSelectedExam('toefl')}
                className={`py-3 px-3.5 rounded-2xl border-2 font-bold text-sm transition-all flex items-center justify-center gap-2 ${
                  selectedExam === 'toefl'
                    ? 'border-amber-400 bg-amber-500/10 text-amber-300 shadow-lg shadow-amber-500/10'
                    : 'border-slate-800 bg-slate-800/40 text-slate-400 hover:bg-slate-800'
                }`}
              >
                🎓 TOEFL 托福
              </button>
            </div>
          </div>

          {/* 2. 科目选择 */}
          <div className="mb-4">
            <label className="block text-[11px] font-bold uppercase tracking-widest text-slate-400 mb-2">
              2. 选择练习科目
            </label>
            <div className="grid grid-cols-2 gap-2.5">
              <button
                onClick={() => setSelectedSection('listening')}
                className={`py-3 px-3.5 rounded-2xl border-2 font-bold text-sm transition-all flex items-center justify-center gap-2 ${
                  selectedSection === 'listening'
                    ? 'border-indigo-400 bg-indigo-500/10 text-indigo-300 shadow-lg shadow-indigo-500/10'
                    : 'border-slate-800 bg-slate-800/40 text-slate-400 hover:bg-slate-800'
                }`}
              >
                🎧 听力专项
              </button>
              <button
                onClick={() => setSelectedSection('reading')}
                className={`py-3 px-3.5 rounded-2xl border-2 font-bold text-sm transition-all flex items-center justify-center gap-2 ${
                  selectedSection === 'reading'
                    ? 'border-indigo-400 bg-indigo-500/10 text-indigo-300 shadow-lg shadow-indigo-500/10'
                    : 'border-slate-800 bg-slate-800/40 text-slate-400 hover:bg-slate-800'
                }`}
              >
                📖 阅读专项
              </button>
            </div>
          </div>

          {/* 3. 训练模式 */}
          <div>
            <label className="block text-[11px] font-bold uppercase tracking-widest text-slate-400 mb-2">
              3. 选择训练模式
            </label>
            <div className="space-y-2.5">
              <button
                onClick={() => usePracticeStore.getState().startPractice('fragment', selectedExam, selectedSection, 5)}
                className="w-full p-3.5 rounded-2xl border-2 border-slate-800 bg-slate-800/40 hover:border-indigo-500 hover:bg-indigo-500/10 transition-all text-left group shadow-sm"
              >
                <div className="font-bold text-white text-sm group-hover:text-indigo-300 flex items-center justify-between">
                  <span>📱 碎片微练模式</span>
                  <span className="text-[11px] bg-indigo-500/20 text-indigo-300 px-2 py-0.5 rounded-lg font-semibold">逐题即时反馈</span>
                </div>
                <div className="text-[11px] text-slate-400 mt-0.5">随机刷题，即选即判，逐题讲解不留题组</div>
              </button>

              <button
                onClick={() => usePracticeStore.getState().startPractice('mock', selectedExam, selectedSection)}
                className="w-full p-3.5 rounded-2xl border-2 border-slate-800 bg-slate-800/40 hover:border-amber-400 hover:bg-amber-500/10 transition-all text-left group shadow-sm"
              >
                <div className="font-bold text-white text-sm group-hover:text-amber-300 flex items-center justify-between">
                  <span>📝 全真模拟演练</span>
                  <span className="text-[11px] bg-amber-500/20 text-amber-300 px-2 py-0.5 rounded-lg font-semibold">
                    {mockQuestionCount(selectedExam, selectedSection)}题 · 全真模拟
                  </span>
                </div>
                <div className="text-[11px] text-slate-400 mt-0.5">沉浸式考场还原，计时交卷并生成详细评估</div>
              </button>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}
