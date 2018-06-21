# airline_review_insight
Contains code which:
- cleanses airline passenger reviews from Skytrax and creates a new csv file
- ipython notebooks which 
    + reads reviews using pandas
    + segregates each sentence in to a separate line for each review
    + Generates Word-Vectors on this corpus using Gensim
    + Generates Sentence-Vectors using the word-vectors for +ve and -ve reviews separately
    + Uses k-means clustering with cosine-distance as the distance metric to generate clusters
    + Perform Cluster Analysis to generate insight - high freq words to indicate what the cluster is about
    + Check if a given paragragh is actually a review or not!
