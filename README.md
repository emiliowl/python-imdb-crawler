## Funny python stuff for handling IMDb ##
+  This is a fun application for handling top 1000 IMDb movies
+ This is far away from production ready project, with a few improvements required before going live
+ This project relies on Flask as web API framework

## How to prepare your environment before running the API
Unfortunately, due to lack on time (you know resources must be restrained), there is no orchestration process for the initial data loading... you will need to do the boring loading process:

0. install the dependencies for this project
> pip install -r requirements.txt

1. from root folder, execute the first crawler. It will generate the first data capture from IMDb website following the format file_n.html (since the page size is 50 at this moment, it will generate from 1 to 951)
> python batch/crawlers/crawler_1000_movies.py

2. After doing the raw data capture, is time to parse and create the input file for next step (the details crawler). This will generate the file movies_source_map.csv which is the input needed for the details crawler (step 3).
Go ahead and execute it:
> python batch/parsers/parser_1000_movies.py

3. Good, you have done the first data capture, is time to deep dive and get detailed information from these movies. This step will take a long time to finalize... basically we're going to IMDb catalog on the web for every single row of our movies_source_map.csv file ... which causes 1000 http requests to be fired and to write a new file on disk (you can find it inside data/details folder). So, well ... be patient (here is a great oportunity to implement better processment speed with aiohttp) [#https://docs.aiohttp.org/en/stable/]
Lets run details crawler now:
> python batch/crawlers/crawler_details.py

4. Yay! We're finally on the final step... so basically all you need to do is run our last parser that will populate the "database" in csv format that will be used by our API (movie_catalog.csv). Now go ahead and run it:
> python batch/crawlers/parser_details.py

## Running the web API

Now that you've setup everything, you can just run the app, again from the root folder of the project:
> python app.py

You can give it a try through the test_client.py app
> python test_client.py

OR through insomnia API client with the collection file at insomnia.json

> Due to lack of time, this couldn't be done in a beter way... but I let a lot of suggestions for improvements on the whatsnext.drawio doc (just use draw.io to open it [#https://draw.io])

Cheers!


