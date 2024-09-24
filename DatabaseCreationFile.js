/* global use, db */
// MongoDB Playground
// Use Ctrl+Space inside a snippet or a string literal to trigger completions.

const database = 'PythonAPIF2024';
const collection = 'Users';

// Create a new database.
use(database);

// Create a new collection.
db.createCollection(collection);

// Insert documents.
db.getCollection(collection).insertMany([
    { name: 'Alice', email: 'alice@example.com', password: 'alice123' },
    { name: 'Bob', email: 'bob@example.com', password: 'bob123' },
    { name: 'Charlie', email: 'charlie@example.com', password: 'charlie123' }
  ]);

// Find documents.
db.getCollection(collection).find({}).pretty();

