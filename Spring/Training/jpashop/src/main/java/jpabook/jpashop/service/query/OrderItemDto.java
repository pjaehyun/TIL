package jpabook.jpashop.service.query;

import jpabook.jpashop.domain.OrderItem;
import lombok.Data;
import lombok.Getter;

/**
 * OSIV를 off 했을 때 지연로딩이 가능하게 하도록 커맨드와 쿼리 분리
 */
@Getter
public class OrderItemDto {
    private String itemName; // 상품명
    private int orderPrice; // 주문 가격
    private int count; // 주문수량
    public OrderItemDto(OrderItem orderItem) {
        itemName = orderItem.getItem().getName();
        orderPrice = orderItem.getOrderPrice();
        count = orderItem.getCount();
    }
}
