package com.jh.jwt.service;

import com.jh.jwt.domain.CustomUserDetails;
import com.jh.jwt.domain.User;
import com.jh.jwt.repository.UserRepository;
import lombok.RequiredArgsConstructor;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.security.core.userdetails.UserDetails;
import org.springframework.security.core.userdetails.UserDetailsService;
import org.springframework.security.core.userdetails.UsernameNotFoundException;
import org.springframework.stereotype.Service;

import java.util.List;

@RequiredArgsConstructor
@Service
public class CustomUserDetailService implements UserDetailsService {

    private final UserRepository userRepository;
    protected final Logger logger = LoggerFactory.getLogger(CustomUserDetailService.class);

    @Override
    public UserDetails loadUserByUsername(String username) throws UsernameNotFoundException {
        List<User> users = userRepository.findByUsername(username);
        if (users.isEmpty()) {
            // Exception
            throw new UsernameNotFoundException("존재하지 않는 회원입니다.");
        }
        return new CustomUserDetails(users.get(0));
    }
}
