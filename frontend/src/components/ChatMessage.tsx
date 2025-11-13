/**
 * ChatMessage komponent - visar ett enskilt meddelande
 */
import type { ChatMessage as ChatMessageType } from '../types/chat';

interface ChatMessageProps {
  message: ChatMessageType;
}

export default function ChatMessage({ message }: ChatMessageProps) {
  return (
    <div className="space-y-4">
      {/* Användarens fråga */}
      <div className="flex justify-end">
        <div className="bg-blue-600 text-white rounded-lg px-4 py-2 max-w-[70%] shadow-md">
          <p className="text-sm">{message.question}</p>
        </div>
      </div>

      {/* Botens svar */}
      <div className="flex justify-start">
        <div className="bg-gray-100 text-gray-900 rounded-lg px-4 py-3 max-w-[70%] shadow-md">
          {message.isLoading ? (
            <div className="flex items-center space-x-2">
              <div className="animate-pulse flex space-x-1">
                <div className="h-2 w-2 bg-gray-400 rounded-full"></div>
                <div className="h-2 w-2 bg-gray-400 rounded-full"></div>
                <div className="h-2 w-2 bg-gray-400 rounded-full"></div>
              </div>
              <span className="text-sm text-gray-500">Tänker...</span>
            </div>
          ) : (
            <p className="text-sm whitespace-pre-wrap">{message.answer}</p>
          )}
          {!message.isLoading && (
            <p className="text-xs text-gray-500 mt-2">
              {new Date(message.timestamp).toLocaleTimeString('sv-SE', {
                hour: '2-digit',
                minute: '2-digit',
              })}
            </p>
          )}
        </div>
      </div>
    </div>
  );
}
