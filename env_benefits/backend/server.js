const express = require("express");
const mongoose = require("mongoose");

const app = express();
const PORT = process.env.PORT || 5000;

const DB_HOST = process.env.DB_HOST || "mongodb";
const DB_PORT = process.env.DB_PORT || "27017";
const DB_NAME = process.env.DB_NAME || "myappdb";

const mongoURL = `mongodb://${DB_HOST}:${DB_PORT}/${DB_NAME}`;

mongoose.connect(mongoURL)
  .then(() => {
    console.log("Connected to MongoDB successfully");
  })
  .catch((error) => {   
    console.log("MongoDB connection error:", error);
  });

app.get("/", (req, res) => {
  res.send("Node.js backend is running and connected to MongoDB using environment variables");
});

app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});