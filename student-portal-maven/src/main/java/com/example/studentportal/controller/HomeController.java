package com.example.studentportal.controller;

import com.example.studentportal.model.Feedback;
import com.example.studentportal.service.MessageService;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.ModelAttribute;
import org.springframework.web.bind.annotation.PostMapping;

@Controller
public class HomeController {

    private final MessageService messageService;

    public HomeController(MessageService messageService) {
        this.messageService = messageService;
    }

    @GetMapping("/")
    public String home(Model model) {
        model.addAttribute("feedback", new Feedback());
        return "index";
    }

    @GetMapping("/about")
    public String about() {
        return "about";
    }

    @PostMapping("/submit")
    public String submit(@ModelAttribute Feedback feedback, Model model) {
        String finalMessage = messageService.buildThankYouMessage(
                feedback.getName(),
                feedback.getMessage()
        );
        model.addAttribute("finalMessage", finalMessage);
        return "result";
    }
}