Purpose
=======
To keep the size of the sherpa repository itself managable, large data files that are only needed for testing are kept in a separate repository. Sherpa tests that need those files are skipped if the sherpa-test-data suite is not present.

Layout of sherpa-test-data
==========================

The following are recommendations for the directory strucure of this repro.
*The rational for each recommendation is set in italics.*

- Data files are stored in the sherpa-test-data/sherpatest/ directory or a sub-directory, no more than 1 level deep. *Since some files are large, we usually want to use the same file in several different tests for several different parts os sherpa. Thus we do NOT want to follow the directory structure of sherpa.*

- Subdirectories are used when multiple files "belong together" for a single dataset, typically src and bkg pha, arf and rmf files or different regions in the same dataset. *Collecting this in a subdirectory makes is easy to find files that belong together and keeps the listing of the "sherpatest" directory short enough to read.*

- Subdirectories shall include a short README describing the data source and shape in words (e.g. "emission lines source with XMM/RGS, low-signal in general, but three bright lines"). *For tests, we usually look for either a specific instrument (e.g. check RMF reading works with XMM/RGS), or shape of spectrum (e.g. chekc powerlaw-fit works on real-world data). The same dataset can be used for both cases.*

- Subdirectories, can, but don't have to, include a short script file with the commands used to generate the test files. *This can helpful if the files need to be updated later, e.g. if a test needs added background files or PHA I instead of PHA II files.*

- If a test only needs one or two files, they stay directly in sherpa-test-data/sherpatest/

- Files <~50 kb or so are placed in sherpa itself and not "sherpa-test-data".  *If the files are part of sherpa itself, tests using them will be run more often and disk space is not a problem for such small files. Also, there is overhead in coordinating PRs to two repros and updating the submodule.*

- These recommendations apply to changes in sherpa-test-data. *We are not spending time to sort existing test files into subdirectories just for the sake of sorting them.*
