const {src, series, dest, watch} = require('gulp');
const sass = require('gulp-sass')(require('sass'));
const postcss = require('gulp-postcss');
const cssnano = require('cssnano');
const terser = require('gulp-terser');
const concat = require('gulp-concat');
const sourcemaps = require('gulp-sourcemaps');



//Task ---> SCSS into CSS
function scssTask(){
    return src('Sakha/static/scss/*.scss')
    .pipe(sass())
    .pipe(postcss([cssnano()]))
    .pipe(dest('Sakha/static/css'));
}




//Task ---> Minifying JavaScript
function minifyJS() {
    return src('Sakha/static/js/*.js')
    .pipe(terser())
    .pipe(dest('Sakha/static/minjs'))
}




/* ---------------------------------JS Files Concatenation Start-------------------------------- */
//Task ---> Concatenating layout.js and followers.js
function layoutFollowersJS() {
    return src(['Sakha/static/minjs/layout.js','Sakha/static/minjs/followers.js'])
    .pipe(sourcemaps.init())
    .pipe(concat('layoutFollowers.js'))
    .pipe(sourcemaps.write('./'))
    .pipe(dest('Sakha/static/minjs'));
}



//Task ---> Concatenating layout.js and home.js
function layoutHomeJS() {
    return src(['Sakha/static/minjs/layout.js','Sakha/static/minjs/home.js'])
    .pipe(sourcemaps.init())
    .pipe(concat('layoutHome.js'))
    .pipe(sourcemaps.write('./'))
    .pipe(dest('Sakha/static/minjs'));
}



//Task ---> Concatenating layout.js and profile.js
function layoutProfileJS() {
    return src(['Sakha/static/minjs/layout.js','Sakha/static/minjs/profile.js'])
    .pipe(sourcemaps.init())
    .pipe(concat('layoutProfile.js'))
    .pipe(sourcemaps.write('./'))
    .pipe(dest('Sakha/static/minjs'));
}



//Task ---> Concatenating layout.js and settings.js
function layoutSettingsJS() {
    return src(['Sakha/static/minjs/layout.js','Sakha/static/minjs/settings.js'])
    .pipe(sourcemaps.init())
    .pipe(concat('layoutSettings.js'))
    .pipe(sourcemaps.write('./'))
    .pipe(dest('Sakha/static/minjs'));
}



//Task ---> Concatenating layout.js and userProfile.js
function layoutUserProfileJS() {
    return src(['Sakha/static/minjs/layout.js','Sakha/static/minjs/userProfile.js'])
    .pipe(sourcemaps.init())
    .pipe(concat('layoutUserProfile.js'))
    .pipe(sourcemaps.write('./'))
    .pipe(dest('Sakha/static/minjs'));
}
/*---------------------------JS Concatenation functions end------------------------------- */





//Task ---> Watch the changes made in SCSS and JS
function watchTask() {
    watch(['Sakha/static/js/*.js', 'Sakha/static/scss/*.scss'], 
            series(scssTask, minifyJS, layoutFollowersJS, layoutHomeJS, 
                    layoutProfileJS, layoutSettingsJS, layoutUserProfileJS));
}





exports.default = series (
    scssTask,
    minifyJS,
    layoutFollowersJS,
    layoutHomeJS, 
    layoutProfileJS,
    layoutSettingsJS,
    layoutUserProfileJS,
    watchTask 
);




















//Task ---> Concatenation of JS Files


// //Task --->  To run browsersync server
// //We have to use callback since browsersync is not in gulp
// function browserSyncServe(cb) {
//     browsersync.init({
//         server : {
//             baseDir : '.'
//         }
//     });
//     cb();
// }




// //Task ---> To reload the browser when changes are made in SCSS and JS
// function browserSyncReload(cb) {
//     browsersync.reload();
//     cb();
// }
