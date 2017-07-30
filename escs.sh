##############################################################################
# clone, isnuts, github.
cd ~/projects
git clone git@github.com:iogf/isnuts.git isnuts-code
##############################################################################
# push, isnuts, github.
cd ~/projects/isnuts-code
git status
git add *
git commit -a
git push 
##############################################################################
# create the develop branch, isnuts.
git branch -a
git checkout -b development
git push --set-upstream origin development
##############################################################################
# merge master into development, isnuts.
cd ~/projects/isnuts-code
git checkout development
git merge master
git push
##############################################################################
# merge development into master, isnuts.
cd ~/projects/isnuts-code
git checkout master
git merge development
git push
git checkout development
##############################################################################
# check diffs, isnuts.
cd ~/projects/isnuts-code
git diff
##############################################################################
# delete the development branch, isnuts.
git branch -d development
git push origin :development
git fetch -p 
##############################################################################
# undo, changes, isnuts, github.
cd ~/projects/isnuts-code
git checkout *
##############################################################################
# create, a new branch locally from an existing commit, from, master.
git checkout master
cd ~/projects/isnuts-code
git checkout -b old_version fcebcd4f229cb29cac344161937d249785bf83f8
git push --set-upstream origin old_version

git checkout old_version
##############################################################################
# delete, old version, isnuts.
git checkout master
git branch -d old_version
git push origin :old_version
git fetch -p 
##############################################################################
# create, toc, table of contents, isnuts.
cd ~/projects/isnuts-code
gh-md-toc BOOK.md > table.md
vy table.md
rm table.md
##############################################################################
# install, isnuts.
sudo bash -i
cd /home/tau/projects/isnuts-code
python setup.py install
rm -fr build
exit
##############################################################################
# build, isnuts, package, disutils.
cd /home/tau/projects/isnuts-code
python setup.py sdist 
rm -fr dist
rm MANIFEST
##############################################################################
# share, put, place, host, package, python, pip, application, isnuts.

cd ~/projects/isnuts-code
python setup.py sdist register upload
rm -fr dist
##############################################################################
# port to py3 code.

cd ~/projects/isnuts-code

# Apply them.
2to3  -w .

find . -name "*.bak" -exec rm -f {} \;





