import wikipedia
import time

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
