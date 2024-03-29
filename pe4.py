import wikipedia
import time
import concurrent.futures

# Part A
# Use wikipedia.search to get a list of topics related to 
'generative artificial intelligence'
topics = wikipedia.search("generative artificial intelligence")

# Iterate over the topics and save references to a .txt file.
start_time = time.perf_counter()  # Start time
for topic in topics:
    # Retrieve page content
    page = wikipedia.page(topic, auto_suggest=False)
    # Get page title
    page_title = page.title
    # Get references
    references = page.references

    # Write references to a .txt file
    with open(f"{page_title}.txt", "w", encoding="utf-8") as f:
        for reference in references:
            f.write(reference + "\n")

# Print the time taken.
end_time = time.perf_counter()  # End time
print("Time taken:", end_time - start_time, "seconds")

# Part B
def wiki_dl_and_save(topic):
    # Retrieve the Wikipedia page for the topic
    page = wikipedia.page(topic, auto_suggest=False)
    # Get the title and references for the topic
    page_title = page.title
    references = page.references
    # Create a .txt file where the name of the file is the title of the topic
    with open(f"{page_title}.txt", "w", encoding="utf-8") as f:
        # Write the references to the file
        for reference in references:
            f.write(reference + "\n")

# Use wikipedia.search to get a list of topics related to 'generative artificial intelligence'
topics = wikipedia.search("generative artificial intelligence")

# Concurrently download Wikipedia content
start_time = time.perf_counter()  # Start time
# Use ThreadPoolExecutor to execute wiki_dl_and_save concurrently for each topic
with concurrent.futures.ThreadPoolExecutor() as executor:
    executor.map(wiki_dl_and_save, topics)

# Print the time taken
end_time = time.perf_counter()  # End time
print("Time taken:", end_time - start_time, "seconds")
