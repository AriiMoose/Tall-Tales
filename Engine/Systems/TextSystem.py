__author__ = 'Andrew Tully'
__copyright__ = 'Copyright 2015, Andrew Tully'
__credits__ = 'Andrew Tully'
__license__ = 'MIT'
__maintainer__ = 'Andrew Tully'
__email__ = 'ariimoose@gmail.com'
__status__ = 'Development'

""" Desc:   * Subclass of the System abstract class
            * Defines logic for the text management and natural language processing

    Usage:  * Text System is subclassed and added to relevant scene
            * Text should be tagged within the event queue
"""

from Engine.System import System
import nltk
from nltk.corpus import brown
from nltk.corpus import wordnet as wn
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
        self.default_tagger = nltk.DefaultTagger('NN')
        self.uni_tagger = nltk.UnigramTagger(self.train_sents, backoff=self.default_tagger)
        self.bi_tagger = nltk.BigramTagger(self.train_sents, backoff=self.uni_tagger)
        self.tri_tagger = nltk.TrigramTagger(self.train_sents, backoff=self.bi_tagger)

        super(TextSystem, self).__init__(type)

    def update(self):
        pass

    def access_components(self):
        # Access the strings within an entity's text component
        for ents in self.entityList:
            if "text" in self.entityList.get(ents).componentList:
                for comps in self.entityList.get(ents).componentList:
                    for strings in self.entityList.get(ents).componentList.get(comps):
                        if strings.input_string is not None:
                            print "Input exists"
                            strings.pos_tags = self.get_pos(strings.input_string)
                            print(strings.pos_tags)
                            self.temp = self.interpret(strings.pos_tags)
                            print(self.temp)
                            strings.action = self.temp[0]
                            print(strings.action)
                            strings.action_target = self.temp[1]

                            print(strings.action_target)
                        else:
                            print "Input not found"


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

    def interpret(self, input_tokens):
        """ Executes the text recognition algorithm on tagged tokens
            Checks the tag for each token until it finds a verb
            Assumes the first verb in the sentence is the operative verb
            Finds the subject of the verb by finding the first noun following the operative verb
            If there is no verb found, then it is assumed that the first or second word is a verb

        Args:
            input_tokens: Tagged tokens to be analysed
        """
        # Regular expression to match with verbs (VB), nouns (NN), and personal prepositions (PPSS)
        reg_verb = re.compile(r'VB')
        reg_noun = re.compile(r'NN')
        reg_prep = re.compile(r'PPSS')

        self.i = 0
        self.operative_verb = None
        self.target_noun = None

        # Check for operative verb
        # If the tag of the token tuple matches with the appropriate regex then record it
        if input_tokens is not None:
            for token in input_tokens:
                if reg_verb.search(token[1]) is not None:
                    print "Matched verb token: " + token.__str__()
                    self.operative_verb = token[0]
                    """
                    if reg_in.search((input_tokens.index(token) + 1)[1]) is not None:
                        current_verb = self.operative_verb
                        self.operative_verb = current_verb + "_" + (input_tokens.index(token) + 1)
                        print("Op. Verb: " + self.operative_verb)
                    """
                    break

            # If no verb is found, assume the first or second word are verbs
            # This circumvents incorrect tagging
            if self.operative_verb is None:
                # If the first word is not a personal preposition, assume that it is a verb
                # input_tokens[0] is the first token in the list of input_tokens
                # (input_tokens[0])[1] is the second part of the tuple at input_tokens[0]
                if reg_prep.search((input_tokens[0])[1]) is None:
                    self.operative_verb = (input_tokens[0])[0]
                else:
                    # Otherwise, assume the second word is a verb
                    self.operative_verb = (input_tokens[1])[0]

            # Check for the noun which is the target of the operative verb
            for token in input_tokens:
                if reg_noun.search(token[1]) is not None and token[0] is not self.operative_verb:
                    print "Matched noun token: " + token.__str__()
                    self.target_noun = token[0]
            """
            Note on Syntax:

                input_tokens is a list of tuples
                In order to access this, we need to access the list element containing the tuple we want. Hence, input_tokens[0]
                Once this is done, we must access the element of the necessary tuple. Hence, (input_tokens[0])[1]
                This accesses the tuple and the element we need.
                In this case it is the first element of the tuple contains the word, while the second contains its tag
            """

            print(self.operative_verb)
            print(self.target_noun)

            # If a verb and accompanying noun were found return them as a tuple
            if self.operative_verb is not None and self.target_noun is not None:
                result_set = [self.operative_verb, self.target_noun]
                return result_set

            # If a verb was found, but no noun was found, return a list with a blank noun
            elif self.operative_verb is not None and self.target_noun is None:
                result_set = [self.operative_verb, ""]
                return result_set

        else:
            result_set = ["", ""]
            return result_set

    def checkInput(cls, action):
        """ - Recursive function
            - Checks user input, if  that fails, check synonyms
            - If there is still no match, return false
        """

        syn_list = []
        out_list = []

        for synset in wn.synsets(action, pos=wn.VERB):
            for lemma in synset.lemmas():
                found = lemma.name()
                print(found)

                syn_list.append(str(found))
                print(syn_list)

                for syn in syn_list:
                    if syn not in out_list:
                        out_list.append(syn)

                print(out_list)

        return out_list