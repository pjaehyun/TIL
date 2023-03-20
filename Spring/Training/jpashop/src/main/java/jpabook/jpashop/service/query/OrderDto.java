package jpabook.jpashop.service.query;

import jpabook.jpashop.domain.Address;
import jpabook.jpashop.domain.Order;
import jpabook.jpashop.domain.OrderStatus;
import lombok.Data;
import lombok.Getter;

import java.time.LocalDateTime;
import java.util.List;

import static java.util.stream.Collectors.toList;

/**
 * OSIV를 off 했을 때 지연로딩이 가능하게 하도록 커맨드와 쿼리 분리
 */
@Getter
public class OrderDto {
    private Long orderId;
    private String name;
    private LocalDateTime orderDate;
    private OrderStatus orderStatus;
    private Address address;
    private List<OrderItemDto> orderItems;
    public OrderDto(Order order) {
        orderId = order.getId();
        name = order.getMember().getName();
        orderDate = order.getOrderDate();
        orderStatus = order.getStatus();
        address = order.getDelivery().getAddress();
        order.getOrderItems().forEach(o -> o.getItem().getName());
        orderItems = order.getOrderItems().stream()
                .map(OrderItemDto::new)
                .collect(toList());
    }
}
