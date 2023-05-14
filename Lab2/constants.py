abbreviations = ['a.m.', 'p.m.', 'Mr.', 'Mrs.', 'Ms.', 'e.g.', 'Jan.', 'Feb.', 'Mar.', 'Apr.', 'Jun.', 'Jul.',
                 'Aug.', 'Sep.', 'Oct.', 'Nov.', 'Dec.']
regular_abbreviations = r'a\.m\.|p\.m\.|Mr\.|Mrs\.|Ms\.|e\.g\.|Jan\.|Feb\.|Mar\.|Apr\.|Jun\.|Jul\.|Aug\.|Sep\.' +\
                        r'|Oct\.|Nov\.|Dec\.'

regular_sentence = r'((([^\.\!\?]*('+regular_abbreviations+r'))*[^\.\?\!]*)[\.\?\!]+)'
regular_word = r'\b[a-z][\w]*\b'
regular_sentence_declarative = r'[^?!]+\.+'