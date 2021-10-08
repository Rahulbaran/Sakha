const {src, series, dest, watch} = require('gulp');
const sass = require('gulp-sass')(require('sass'));
const postcss = require('gulp-postcss');
const cssnano = require('cssnano');
const terser = require('gulp-terser');
const sourcemaps = require('gulp-sourcemaps');
const browsersync = require('browser-sync').create();



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
    .pipe(sourcemaps.init())
    .pipe(terser())
    .pipe(sourcemaps.write('./'))
    .pipe(dest('Sakha/static/minjs'))
}




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



//Task ---> Watch the changes made in SCSS and JS
function watchTask() {
    watch(['Sakha/static/js/*.js', 'Sakha/static/scss/*.scss'], 
            series(scssTask, minifyJS));
}






exports.default = series (
    scssTask,
    minifyJS,
    watchTask 
);


