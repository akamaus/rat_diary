from rat_journal import *

date("2016-01-26")
cage(1)

rat(1).trace("1:10(1)->2:10(2)[c]->3:10(T)")
rat(2).trace("2:10(1)->3:10(c)")

cage(2)
rat(3).trace("1:10(c)->2:10(2)[c][d]->3:10(T)")
rat(4).trace("2:10(1)->3:10(c)")

date("2016-01-27")

cage(1)
rat(1).trace("1:10(c)->2:10(2)->3:10(T)")
rat(2).trace("2:10(1)->3:10(c)")

print_full_journal()
