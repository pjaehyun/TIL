package com.jh.jwt.exception;

public class NotLoggedInException extends RuntimeException {
    public NotLoggedInException() {
    }

    public NotLoggedInException(String message) {
        super(message);
    }

    public NotLoggedInException(String message, Throwable cause) {
        super(message, cause);
    }

    public NotLoggedInException(Throwable cause) {
        super(cause);
    }
}
