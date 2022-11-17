package hello.core;

import org.springframework.context.annotation.ComponentScan;
import org.springframework.context.annotation.Configuration;
import org.springframework.context.annotation.FilterType;

@Configuration
@ComponentScan(
        // 만약 지정하지 않으면 @ComponentScan이 붙은 설정 정보 클래스의 패키지가 시작위치가 됨
//        basePackages = "hello.core", // 탐색할 패키지의 시작 위치 지정, 패키지 포함하여 하위 패키지 모두 탐색
//        basePackageClasses = AutoAppConfig.class,
        excludeFilters = @ComponentScan.Filter(type = FilterType.ANNOTATION, classes = Configuration.class)
)

public class AutoAppConfig {

}
