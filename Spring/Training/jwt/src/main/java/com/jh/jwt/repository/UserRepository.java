package com.jh.jwt.repository;

import com.jh.jwt.domain.User;
import org.springframework.stereotype.Repository;

import javax.persistence.EntityManager;
import javax.persistence.PersistenceContext;
import java.util.List;

@Repository
public class UserRepository{
    @PersistenceContext
    private EntityManager em;

    public Long save(User user) { em.persist(user); return user.getId();}

    public List<User> findByUsername(String username) {
        return em.createQuery("select u from User u where u.username = :username", User.class)
                .setParameter("username", username)
                .getResultList();
    }

    public User findOne(Long id) { return em.find(User.class, id);}
}
