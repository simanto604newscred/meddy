Meddy Assignment

# Run aggregator webservice 
`docker-compose up`
# Run tests
`docker exec -ti aggregator_webservice "pytest"`

# Assessment tasks 
- [X]  My code follows the code style guide of pep8.
- [ ]  Python Proficiency (For Reviewers)
- [X]  Ability to understand and use 3rd party APIs
- [X]  Ability to parse different forms of data
- [X]  Ability to write unit tests, test coverage is 95%
- [X]  Ability to write documentation (tried self descriptive source as much as I could)
- [X]  Generally professional code that follows standards in matter of commits and security (tried to make understandle commit messages)

# Improvement points
- [ ]  Use distributed cache like Redis (NOTED in source with todo)
- [ ]  Use async request client like `aiohttp` and test showing the difference (NOTED in source with todo)
- [ ]  Use basic authentication
- [ ]  Improvement on test coverage for edge case based exception handling
- [ ]  Add pagination support for both providers and clients consumtion. 

# How to add new source/providers API
* 
