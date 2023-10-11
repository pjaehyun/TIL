package com.jh.jwt.service;

import com.jh.jwt.controller.LoginResponseDto;
import com.jh.jwt.controller.UserController;
import com.jh.jwt.domain.Authority;
import com.jh.jwt.domain.CustomUserDetails;
import com.jh.jwt.domain.User;
import com.jh.jwt.repository.UserRepository;
import com.jh.jwt.utils.RedisUtil;
import com.jh.jwt.utils.TokenProvider;
import lombok.RequiredArgsConstructor;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.security.authentication.BadCredentialsException;
import org.springframework.security.authentication.UsernamePasswordAuthenticationToken;
import org.springframework.security.config.annotation.authentication.builders.AuthenticationManagerBuilder;
import org.springframework.security.core.Authentication;
import org.springframework.security.core.userdetails.UsernameNotFoundException;
import org.springframework.security.crypto.bcrypt.BCryptPasswordEncoder;
import org.springframework.security.crypto.password.PasswordEncoder;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

import javax.servlet.http.HttpServletRequest;
import java.util.*;

@Service
@RequiredArgsConstructor
public class UserService {

    private final UserRepository userRepository;
    private final AuthenticationManagerBuilder authenticationManagerBuilder;

    private final RedisUtil redisUtil;
    protected final Logger logger = LoggerFactory.getLogger(UserService.class);

    private final PasswordEncoder passwordEncoder;
    private final TokenProvider tokenProvider;

    @Transactional
    public Long join(String username, String password, String auth){
        User user = User.builder()
                .username(username)
                .password(passwordEncoder.encode(password))
                .authority(Authority.valueOf(auth))
                .build();
        return userRepository.save(user);
    }

    @Transactional
    public LoginResponseDto login(String username, String password){
        // 회원 validation
        List<User> users = userRepository.findByUsername(username);
        if (users.isEmpty()) {
            throw new UsernameNotFoundException("존재하지 않는 회원입니다.");
        }
//         비밀번호 체크
        if (!passwordEncoder.matches(password, users.get(0).getPassword())) {
            throw new BadCredentialsException("비밀번호가 틀렸습니다.");
        }


        UsernamePasswordAuthenticationToken authenticationToken = new UsernamePasswordAuthenticationToken(username, password);
        logger.debug("JwtAuthenticationFilter : 토큰생성완료");

        Authentication authentication = authenticationManagerBuilder.getObject().authenticate(authenticationToken);
        CustomUserDetails principal = (CustomUserDetails) authentication.getPrincipal();

        String accessToken = tokenProvider.createAccessJwt(principal);
        String refreshToken = tokenProvider.createRefreshJwt(principal);

        users.get(0).setRefreshToken(refreshToken);


        return LoginResponseDto.builder().accessToken(accessToken).refreshToken(refreshToken).build();
    }

    public LoginResponseDto refresh(HttpServletRequest request) {
        String refreshToken = tokenProvider.resolveToken(request);
        boolean validate = tokenProvider.validateRefreshToken(refreshToken);

        String username = tokenProvider.getRefreshUsername(refreshToken);
        List<User> user = userRepository.findByUsername(username);

        if (!user.get(0).getRefreshToken().equals(refreshToken)){
            throw new BadCredentialsException("바보");
        }

        CustomUserDetails cud = new CustomUserDetails(user.get(0));

        String newAccessToken = tokenProvider.createAccessJwt(cud);
        String newRefreshToken = tokenProvider.createRefreshJwt(cud);
        return LoginResponseDto.builder().accessToken(newAccessToken).refreshToken(newRefreshToken).build();
    }

    // 레디스 블랙리스트에 accessToken값을 저장
    public String logout(HttpServletRequest request) {
        String accessToken = tokenProvider.resolveToken(request);
        String username = tokenProvider.getUsername(accessToken);
        List<User> user = userRepository.findByUsername(username);

        user.get(0).setRefreshToken("");
        redisUtil.setBlackList(accessToken, "accessToken", 5);
        return "로그아웃";
    }
}
