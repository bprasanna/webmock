import sqlite3

def add_mock_content(url):
	# Create database
	conn = sqlite3.connect('webmock.db')

	# Get cursor
	c = conn.cursor()

	# Retrieve content from url


	# Create table
	c.execute('''CREATE VIRTUAL TABLE IF NOT EXISTS mock_content UNSING fts3(url, question_count, question , answer, keywords, score)''')

	# Insert a row of data
	c.execute("INSERT INTO mock_content VALUES ('2006-01-05','BUY','RHAT',100,35.14)")\

	# Save (commit) the changes
	conn.commit()

	# We can also close the connection if we are done with it.
	# Just be sure any changes have been committed or they will be lost.
	conn.close()
