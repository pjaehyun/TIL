package com.jh.jwt.utils;

import lombok.RequiredArgsConstructor;
import org.springframework.data.redis.connection.Message;
import org.springframework.data.redis.connection.MessageListener;
import org.springframework.data.redis.core.RedisTemplate;

@RequiredArgsConstructor
public class KeyExpiredMessageListener implements MessageListener {

    @Override
    public void onMessage(Message message, byte[] pattern) {
        RedisTemplate<String, Object> redisTemplate = new RedisTemplate<>();
        String expiredKey = message.toString();
        redisTemplate.delete(expiredKey);

    }
}
