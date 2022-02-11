# Import package
import wikipedia
import openai
import os
import json
from time import sleep

openai.api_key = "key-goes-here"

example_answer = "According to the Texas Relocation Report 2021, more than 500,000 people relocated to the state in 2019. Tesla founder Elon Musk also recently announced his decision to move to Texas. The state has welcomed more than 200,000 residents from outside the country in the same year as well.\n\nThe Texas Relocation Report was created after gathering information from the U.S. Census Bureau. It was compiled by Texas Realtors.\n\nBut this is not a recent trend. A lot of people have been moving to Texas for some time now. There is increased demand for a Texas moving company for cities like Houston, Dallas, Fort Worth, and San Antonio. According to reports, 4.2 million people have moved to the state since the last census in 2010, which is a growth of 16.4%. This places Texas just behind the 17.4% population growth rate of Utah.\n\nMore Than 500,000 People Move to Texas for 7 Straight Years\n\nWhile so many people are moving to Texas, a few of the state’s residents are also moving out. But even then, The Lone Star State reports an overall gain of 100,000 new residents for 2019.\n\nIt is the 7th year in a row that the state has seen a 500,000 plus inflow of residents. Most of the Texas movers are from California and Florida. The U.S. Census Bureau data says that more than 687,000 Californians have moved to Texas over the last decade.\n\nDallas, Austin Both Popular for Relocation\n\nLouisiana, Oklahoma, Illinois, Georgia, New Mexico, and Arizona are the other top states from where the residents are moving to Texas. Austin, Midland, San Antonio, Dallas-Fort Worth, and Houston are the most popular cities. According to a report published by the Redfin real estate brokerage firm on February 4, the city of Dallas is attracting a lot of inflows. Job website LinkedIn, on the other hand, reports that Austin has attracted many professionals, especially during the pandemic.\n\nTop Reasons Why So Many Are Moving to Texas\n\n1. Jobs – The gas and oil boom has turned Texas into an economic powerhouse. Houston, especially, has emerged as the world energy capital. There have also been strong growths in business services, manufacturing, and the technology sector. The state also has a strong military presence, boosted by increased defense spending after 9/11. Many businesses are relocating to Texas because of the high number of university graduates.\n\nMany Dallas movers say they are moving not just for more employment opportunities but also for higher wages. For example, in Dallas, the average annual wage is $67,500. The state’s average salary is around $38,000, which is $9,000 higher than the national average.\n\n2. Texas is cheaper – For most people, the San Francisco Bay Area and New York are both too expensive. Houston, on the other hand, is much cheaper. So your paycheck will go much more here. Houston has a low cost of living, thanks to the lower transport and utility costs, consumer prices, and housing feel the CEO of  Austin Movers. It is likely to stay that way for a while, feels the CEO.\n\nIn Houston, the ratio of median home price to median annual household income is just 2.9. In San Francisco, it is 6.7. In LA, SF, and NYC, most people are always struggling to make ends meet."
# Specify the title of the Wikipedia page
wiki = wikipedia.page('Hermiston, Oregon')

text_raw = wiki.content

example_context_text = "Texas is a state in the South Central region of the United States  At 268,596 square miles (695,662 km2), and with more than 29.1 million residents in 2020, it is the second-largest U S  state by both area (after Alaska) and population (after California)  Texas shares borders with the states of Louisiana to the east, Arkansas to the northeast, Oklahoma to the north, New Mexico to the west, and the Mexican states of Chihuahua, Coahuila, Nuevo León, and Tamaulipas to the south and southwest; and has a coastline with the Gulf of Mexico to the southeast."

# text = json.dumps(text_raw)

# text_file = open("text.jsonl", "w")
# n = text_file.write("{\"text\": " + text + "}")
# text_file.close()
#
# ret_val = openai.File.create(file=open("text.jsonl"), purpose='answers')
# print(ret_val["id"])

response = openai.Answer.create(
    search_model="ada",
    model="davinci",
    question="Should I move to Hermiston, Oregon?",
    # file=ret_val["id"],
    documents = [text_raw],
    examples_context=example_context_text,
    examples=[["What are the top reasons to move to Texas?", example_answer]],
    max_rerank=10,
    max_tokens=500,
    stop=["\n", "<|endoftext|>"]
)

print(response)
