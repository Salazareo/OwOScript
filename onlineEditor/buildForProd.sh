rm -rf ../ZIP_ME/
# Transpile .ts to .js
tsc --sourceMap false

cp -r public ./build/
cp package.json ./build/
mkdir ../ZIP_ME

mv ./build ../ZIP_ME/build

cp ../*.py ../ZIP_ME/

cd ../ZIP_ME/build
npm install --only=prod
