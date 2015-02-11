__author__ = 'Andrew Tully'
__copyright__ = 'Copyright 2015, Andrew Tully'
__credits__ = 'Andrew Tully'
__license__ = 'MIT'
__maintainer__ = 'Andrew Tully'
__email__ = 'ariimoose@gmail.com'
__status__ = 'Development'

""" Desc:   * Subclass of the System abstract class
            * Defines logic for the text management and natural language processing

    Usage:  * Text System is added to relevant scene
            * Text should be tagged within the event queue
"""

from Engine.System import System
import nltk
from nltk.corpus import brown
import re

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
        self.default_tagger = nltk.DefaultTagger('VB')
        self.uni_tagger = nltk.UnigramTagger(self.train_sents, backoff=self.default_tagger)
        self.bi_tagger = nltk.BigramTagger(self.train_sents, backoff=self.uni_tagger)
        self.tri_tagger = nltk.TrigramTagger(self.train_sents, backoff=self.bi_tagger)

        super(TextSystem, self).__init__(type)

    def update(self):
        """
        """
        #self.access_components()
        #self.tagged_string = self.get_pos("Open the door")
        #self.interperate(self.tagged_string)


    def access_components(self):
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

            # Tagger Accuracy
            print "Tagger Accuracy:"
            print(self.tri_tagger.evaluate(self.test_sents))

            # Tag user input using multiple backup taggers
            print "Tagging input..."
            self.tagged_output = self.tri_tagger.tag(self.tokens)
            print "" + self.tagged_output.__str__()
            return self.tagged_output

    def interperate(self, input_tokens):
        """ Executes the text recognition algorithm on tagged tokens
            Checks the tag for each token until it finds a verb
            Assumes the first verb in the sentence is the operative verb
            Finds the subject of the verb by finding the first noun following the operative verb

        Args:
            input_tokens: Tagged tokens to be analysed
        """

        reg_verb = re.compile(r'VB')
        reg_noun = re.compile(r'NN')
        self.i = 0
        self.operative_verb = None
        self.target_noun = None

        # Check for operative verb
        for token in input_tokens:
            if reg_verb.search(token[1]) is not None:
                print "Matched verb token: " + token.__str__()
                self.operative_verb = token
                self.i = self.i + 1
                break

            self.i = self.i + 1
        print self.i

        for token in input_tokens[self.i:]:
            if reg_noun.search(token[1]) is not None:
                print "Matched noun token: " + token.__str__()
                self.target_noun = token
                break

        # If a match for the operative verb and target noun is found
        if self.operative_verb is not None and self.target_noun is not None:
            return self.operative_verb, self.target_noun