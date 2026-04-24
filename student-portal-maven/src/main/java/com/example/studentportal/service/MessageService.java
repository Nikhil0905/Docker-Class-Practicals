package com.example.studentportal.service;

import org.springframework.stereotype.Service;

@Service
public class MessageService {

    public String buildThankYouMessage(String name, String message) {
        return "Thank you, " + name + "! Your message was: " + message;
    }
}