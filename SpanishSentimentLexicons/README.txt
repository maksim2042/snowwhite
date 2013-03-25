
Sentiment Lexicons in Spanish
=====================================
Version 1.0
March 11th, 2012

Veronica Perez-Rosas, Carmen Banea and Rada Mihalcea

Language and Information Technologies
University of North Texas

veronica.perezrosas@gmail.com
carmen.banea@gmail.com
rada@cs.unt.edu



CONTENTS
1. Introduction
2. Lexicons
2.a. Annotation
3. Feedback
4. Citation Info
5. Acknowledgments


=======================
1. Introduction

This README v1.0 (March, 2012) for Sentiment Lexicons in Spanish comes from the archive hosted at the following URL:
http://lit.csci.unt.edu/

=======================
2. Lexicon

The lexicons are provided in plain text format. The folder contains two files: fullStrengthLexicon and mediumStrengthLexicon.

The fullStrengthLexicon file contains a Spanish sentiment lexicon which is more robust, as it leverages manual sentiment annotations from the OpinionFinder lexicon (Wiebe et al., 2005).

The mediumStrengthLexicon file contains a lexicon that leverages automatic annotations induced based on SentiWordNet (Essuli and Sebastiani, 2006).

=====
2.a. Data Annotation

The format for both lexicons is as follows:

Spanish_word  Synset_offset_in_WN_1_6  English_annotation  [Spanish_annotation]

where,

Spanish_word is a Spanish word without diacritic marks.

Synset_offset_in_WN_1_6 is the synset offset corresponding to WordNet 1.6.

English_annotation is the corresponding sentiment annotation that was automatically generated using the methods described in the paper referenced below.

[Spanish annotation] is a manual sentiment annotation provided by two Spanish native speakers. Note: this annotation in available only for the first 100 words in each
lexicon.

=======================
3. Feedback

For further questions or inquiries about this data set, you can contact: Veronica Perez (veronica.perezrosas@gmail.com), Carmen Banea (carmen.banea@gmail.com) or Rada Mihalcea (rada@cs.unt.edu).


=======================
4. Citation Info

If you use these lexicons please cite:

@InProceedings{Perez12,
  author =       {Veronica Perez Rosas , Carmen Banea, Rada Mihalcea},
  title =            {Learning Sentiment Lexicons in Spanish},
  booktitle =    {Proceedings of the international conference on Language
                        Resources and Evaluation (LREC)},
  address =      {Istanbul, Turkey},
  year =            {2012}
}

=======================
5. Acknowledgments

This material is based in part upon work supported by National Science Foundation award #0917170. Any opinions, findings, and conclusions or recommendations expressed in this material are those of the authors and do not necessarily reflect the views of the National Science Foundation.

