import text_stats
#Text from 'http://en.wikipedia.org/wiki/Electric_charge'
wiki_text = """ Electric charge is the physical property of matter that causes
                it to experience a force when placed in an electromagnetic
                field. There are two types of electric charges: positive and
                negative. Positively charged substances are repelled from
                other positively charged substances, but attracted to
                negatively charged substances; negatively charged substances
                are repelled from negative and attracted to positive. An
                object is negatively charged if it has an excess of electrons,
                and is otherwise positively charged or uncharged. The SI
                derived unit of electric charge is the coulomb (C), although
                in electrical engineering it is also common to use the
                ampere-hour (Ah), and in chemistry it is common to use the
                elementary charge (e) as a unit. The symbol Q is often used to
                denote charge. The early knowledge of how charged substances
                interact is now called classical electrodynamics, and is still
                very accurate if quantum effects do not need to be considered.
                The electric charge is a fundamental conserved property of
                some subatomic particles, which determines their
                electromagnetic interaction. Electrically charged matter is
                influenced by, and produces, electromagnetic fields. The
                interaction between a moving charge and an electromagnetic
                field is the source of the electromagnetic force, which is one
                of the four fundamental forces (See also: magnetic field).
                Twentieth-century experiments demonstrated that electric
                charge is quantized; that is, it comes in integer multiples
                of individual small units called the elementary charge, e,
                approximately equal to 1.602×10−19 coulombs (except for
                particles called quarks, which have charges that are integer
                multiples of e/3). The proton has a charge of +e, and the
                electron has a charge of −e. The study of charged particles,
                and how their interactions are mediated by photons, is called
                quantum electrodynamics.
            """

#TODO add option for input parameters, maybe use file or url
def main():
    word_stats = text_stats.text_stats()
    word_stats.extract_stats(wiki_text)
    word_stats.print_sorted_dictionary(word_stats.freq_table)

if __name__ == '__main__':
    main()
