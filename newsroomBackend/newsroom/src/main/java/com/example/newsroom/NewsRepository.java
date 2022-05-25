package com.example.newsroom;

import com.google.gson.Gson;
import com.mongodb.*;
import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

import java.util.ArrayList;

@RestController
public class NewsRepository {
    @CrossOrigin(origins="http://localhost:3000")
    @GetMapping("/get")
    public ArrayList<News> getData() {
        MongoClientURI uri = new MongoClientURI("mongodb://admin:password@3.82.214.186:27017");
        MongoClient mongoClient = new MongoClient(uri);
        DB database = mongoClient.getDB("newsweb");
        BasicDBObject searchQuery = new BasicDBObject();
        DBCollection collection = database.getCollection("articles");
        DBCursor cursor = collection.find();

        Gson g = new Gson();
        ArrayList<News> news = new ArrayList<>();
        while (cursor.hasNext()) {
            BasicDBObject obj = (BasicDBObject) cursor.next();

            News n = g.fromJson(obj.toString(), News.class);
            news.add(n);
        }

        for (News news1: news)
            System.out.println(news1.body);

        return news;
    }

}
