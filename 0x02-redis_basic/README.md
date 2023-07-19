# 0x02. Redis basic

Redis is an open-source, in-memory data structure store that can be used as a database, cache, or message broker. It provides a fast and efficient way to store and retrieve data by keeping it entirely in memory. Redis supports a wide range of data structures, including strings, lists, sets, and hashes, and provides atomic operations for manipulating these structures. It is known for its high performance, scalability, and versatility, making it a popular choice for use cases requiring fast data access, caching, real-time analytics, and pub/sub messaging.

Redis has a client-server architecture and uses a request-response model. This means that you (the client) connect to a Redis server through TCP connection, on port 6379 by default. You request some action (like some form of reading, writing, getting, setting, or updating), and the server serves you back a response.

There can be many clients talking to the same server, which is really what Redis or any client-server application is all about. Each client does a (typically blocking) read on a socket waiting for the server response.

### Learning Objectives

- Learn how to use redis for basic operations
- Learn how to use redis as a simple cache
