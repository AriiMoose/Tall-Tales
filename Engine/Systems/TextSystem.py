__author__ = 'Andrew Tully'
__copyright__ = 'Copyright 2015, Andrew Tully'
__credits__ = 'Andrew Tully'
__license__ = 'MIT'
__maintainer__ = 'Andrew Tully'
__email__ = 'ariimoose@gmail.com'
__status__ = 'Development'

""" Desc:   * Subclass of the System abstract class
            * Defines logic for the text management and natural language processing

    Usage:
"""

#!/usr/bin/env python

from Engine.System import System
import nltk
from nltk.corpus import brown

class TextSystem(System):

    def __init__(self):
        #nltk.download()
        self.type = "text"

        # Code taken from 'Natural Language Processing with Python' by Steven Bird. Pg. 203
        # Categorise training & test data
        print "Generating training & test data..."
        self.brown_tagged_sents = brown.tagged_sents(categories='news')

        # Use 90% to construct a model & 10% to test the model
        size = int(len(self.brown_tagged_sents) * 0.9)
        self.train_sents = self.brown_tagged_sents[:size]
        self.test_sents = self.brown_tagged_sents[size:]

        # Setup multiple backup taggers
        print "Creating taggers..."
        self.default_tagger = nltk.DefaultTagger('NN')
        self.uni_tagger = nltk.UnigramTagger(self.train_sents, backoff=self.default_tagger)
        self.bi_tagger = nltk.BigramTagger(self.train_sents, backoff=self.uni_tagger)
        self.tri_tagger = nltk.TrigramTagger(self.train_sents, backoff=self.bi_tagger)

        super(TextSystem, self).__init__(type)

    def update(self):
        """
        """

        # Access the strings within an entity's text component
        for ents in self.entityList:
            if "text" in self.entityList.get(ents).componentList:
                for comps in self.entityList.get(ents).componentList:
                    for strings in self.entityList.get(ents).componentList.get(comps):
                        self.get_pos(strings.input_string)

    def get_pos(self, input_text):
        """ Accepts a string as input
            Tokenises the string & trains the taggers before tagging

        Args:
            input_text: String to be tagged
        """

        # If the input is not an empty string, tokenise
        if input_text is not "":
            print "Tokenising..."
            self.tokens = nltk.word_tokenize(input_text)

            self.tri_tagger.evaluate(self.test_sents)

            # Tag user input using multiple backup taggers
            print "Tagging input..."
            self.tagged_output = self.tri_tagger.tag(input_text)