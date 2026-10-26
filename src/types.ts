export type PracticeMode = 'fragment' | 'mock';
export type ExamType = 'toeic' | 'toefl';
export type SectionType = 'listening' | 'reading';

export interface Question {
  id: string;
  exam: ExamType;
  section: SectionType;
  part: number;
  audio?: string;
  passage?: string;
  question: string;
  options: string[];
  answer: number;
  explanation: string;
}

export interface PracticeSession {
  mode: PracticeMode;
  exam: ExamType;
  section: SectionType;
  questions: Question[];
  answers: (number | null)[];
  currentIndex: number;
  startTime: number;
  elapsedSeconds?: number; // 保存已流逝秒数（页面刷新后恢复计时）
  isFinished: boolean;
  /** 碎片模式累计统计（单题流） */
  stats?: { answered: number; correct: number };
}

export interface PracticeResult {
  total: number;
  correct: number;
  wrong: number;
  unanswered: number;
  accuracy: number;
  timeUsedSec: number;
  wrongQuestions: Question[];
}
