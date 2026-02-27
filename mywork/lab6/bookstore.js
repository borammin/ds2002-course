// Task 2: use database
use bookstore

// Task 3: insert first author
db.authors.insertOne({
  "name": "Jane Austen",
  "nationality": "British",
  "bio": {
    "short": "English novelist known for novels about the British landed gentry.",
    "long": "Jane Austen was an English novelist whose works critique and comment upon the British landed gentry at the end of the 18th century. Her most famous novels include Pride and Prejudice, Sense and Sensibility, and Emma, celebrated for their wit, social commentary, and masterful character development."
  }
})

// Task 4: update to add birthday
db.authors.updateOne(
  { name: "Jane Austen" },
  { $set: { birthday: "1775-12-16" } }
)

// Task 5: insert four more authors
db.authors.insertMany([
  {
    "name": "J.K. Rowling",
    "nationality": "British",
    "bio": {
      "short": "Author of the Harry Potter series.",
      "long": "J.K. Rowling is a British author best known for writing the Harry Potter fantasy series, which has won multiple awards and sold more than 500 million copies worldwide."
    },
    "birthday": "1965-07-31"
  },
  {
    "name": "Rick Riordan",
    "nationality": "American",
    "bio": {
      "short": "Author of the Percy Jackson series.",
      "long": "Rick Riordan is an American author best known for the Percy Jackson & the Olympians series, which blends mythology and modern adventure for young readers."
    },
    "birthday": "1964-06-05"
  },
  {
    "name": "Rachel Renée Russell",
    "nationality": "American",
    "bio": {
      "short": "Author of the Dork Diaries series.",
      "long": "Rachel Renée Russell is an American author and attorney, best known for writing the Dork Diaries series, a humorous series about middle school life."
    },
    "birthday": "1959-03-13"
  },
  {
    "name": "Mary Shelley",
    "nationality": "British",
    "bio": {
      "short": "Author of Frankenstein.",
      "long": "Mary Shelley was a British novelist, best known for writing the Gothic novel Frankenstein, considered a landmark work of science fiction."
    },
    "birthday": "1797-08-30"
  }
])

// Task 6: total count
db.authors.countDocuments()

// Task 7: British authors, sorted by name
db.authors.find({ nationality: "British" }).sort({ name: 1 })