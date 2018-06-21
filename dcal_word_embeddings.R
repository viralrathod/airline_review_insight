library(tidyverse)
library(tidytext)

setwd("/Users/vrathod/Documents/MyPaperPresentations/DCAL/data")
dcal_data <- read.csv("cleansed_dcal_data.csv", stringsAsFactors = F)
dcal_data <- dcal_data %>% mutate(X = NULL, url = NULL, postID = row_number())
dcal_data <- dcal_data %>% mutate(ReviewText = Review_Text_Clean)

unigram_probs <- dcal_data %>%
  unnest_tokens(word, ReviewText) %>%
  count(word, sort = TRUE) %>%
  mutate(p = n / sum(n))

unigram_probs

tidy_skipgrams <- dcal_data %>%
  unnest_tokens(ngram, ReviewText, token = "ngrams", n = 8) %>%
  mutate(ngramID = row_number()) %>% 
  unite(skipgramID, postID, ngramID) %>%
  unnest_tokens(word, ngram)

tidy_skipgrams

library(widyr)

skipgram_probs <- tidy_skipgrams %>%
  pairwise_count(word, skipgramID, diag = TRUE, sort = TRUE) %>%
  mutate(p = n / sum(n))

normalized_prob <- skipgram_probs %>%
  filter(n > 20) %>%
  rename(word1 = item1, word2 = item2) %>%
  left_join(unigram_probs %>%
              select(word1 = word, p1 = p),
            by = "word1") %>%
  left_join(unigram_probs %>%
              select(word2 = word, p2 = p),
            by = "word2") %>%
  mutate(p_together = p / p1 / p2)

normalized_prob %>% 
  filter(word1 == "food") %>%
  arrange(-p_together)

