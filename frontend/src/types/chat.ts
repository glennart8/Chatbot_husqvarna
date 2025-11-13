/**
 * TypeScript typer för chat-applikationen
 */

export interface ChatMessage {
  id: string;
  question: string;
  answer: string;
  timestamp: Date;
  isLoading?: boolean;
}

export interface ChatRequest {
  question: string;
  session_id?: string;
}

export interface ChatResponse {
  answer: string;
  question: string;
  session_id?: string;
  timestamp: string;
}

export interface HealthResponse {
  status: string;
  version: string;
  model_loaded: boolean;
}
