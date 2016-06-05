#!/usr/bin/env bash
shopt -q extglob globstar; extglob_set=$?
((extglob_set)) && shopt -s extglob globstar
mkdir tmp
wget http://central.maven.org/maven2/com/thaiopensource/trang/20091111/trang-20091111.jar -O ./tmp/trang.jar
java -jar ./tmp/trang.jar -I xml -O rng $ANDROID_HOME/samples/**/!(AndroidManifest*).xml ./tmp/android.rng
java -jar ./tmp/trang.jar -I xml -O rng $ANDROID_HOME/samples/**/!(tests)/AndroidManifest.xml ./tmp/manifest.rng
cd autoload/xml/
rng2vim ../../tmp/android.rng android
rng2vim ../../tmp/manifest.rng manifest
rm -rf ../../tmp
((extglob_set)) && shopt -u extglob
