$(function () {
  var $mybook = $("#mybook");
  var $bttn_next = $("#next_page_button");
  var $bttn_prev = $("#prev_page_button");
  var $loading = $("#loading");
  var $mybook_images = $mybook.find("img");
  var cnt_images = $mybook_images.length;
  var loaded = 0;

  $mybook_images.each(function () {
    var $img = $(this);
    var source = $img.attr("src");
    $("<img/>")
      .load(function () {
        ++loaded;
        if (loaded == cnt_images) {
          $loading.hide();
          $bttn_next.show();
          $bttn_prev.show();
          $mybook.show().booklet({
            name: null, //
            width: 800, //
            height: 500, //
            speed: 600, //
            direction: "LTR", //
            //
            next: $bttn_next, //
            prev: $bttn_prev, //
          });
          Cufon.refresh();
        }
      })
      .attr("src", source);
  });
});
$(function () {
  var $mybookAviation = $("#mybookAviation");
  var $bttn_next = $("#next_page_button");
  var $bttn_prev = $("#prev_page_button");
  var $loading = $("#loading");
  var $mybookAviation_images = $mybookAviation.find("img");
  var cnt_images = $mybookAviation_images.length;
  var loaded = 0;

  $mybookAviation_images.each(function () {
    var $img = $(this);
    var source = $img.attr("src");
    $("<img/>")
      .load(function () {
        ++loaded;
        if (loaded == cnt_images) {
          $loading.hide();
          $bttn_next.show();
          $bttn_prev.show();
          $mybookAviation.show().booklet({
            name: null, //
            width: 800, //
            height: 500, //
            speed: 600, //
            direction: "LTR", //
            //
            next: $bttn_next, //
            prev: $bttn_prev, //
          });
          Cufon.refresh();
        }
      })
      .attr("src", source);
  });
});

$(function () {
  var $mybookEducation = $("#mybookEducation");
  var $bttn_next1 = $("#next_page_button1");
  var $bttn_prev1 = $("#prev_page_button1");
  var $loading = $("#loading");
  var $mybookEducation_images = $mybookEducation.find("img");
  var cnt_images = $mybookEducation_images.length;
  var loaded = 0;

  $mybookEducation_images.each(function () {
    var $img = $(this);
    var source = $img.attr("src");
    $("<img/>")
      .load(function () {
        ++loaded;
        if (loaded == cnt_images) {
          $loading.hide();
          $bttn_next1.show();
          $bttn_prev1.show();
          $mybookEducation.show().booklet({
            name: null, //
            width: 800, //
            height: 500, //
            speed: 600, //
            direction: "LTR", //
            //
            next: $bttn_next1, //
            prev: $bttn_prev1, //
          });
          Cufon.refresh();
        }
      })
      .attr("src", source);
  });
});

$(function () {
  var $mybookFood = $("#mybookFood");
  var $bttn_next1 = $("#next_page_button1");
  var $bttn_prev1 = $("#prev_page_button1");
  var $loading = $("#loading");
  var $mybookFood_images = $mybookFood.find("img");
  var cnt_images = $mybookFood_images.length;
  var loaded = 0;

  $mybookFood_images.each(function () {
    var $img = $(this);
    var source = $img.attr("src");
    $("<img/>")
      .load(function () {
        ++loaded;
        if (loaded == cnt_images) {
          $loading.hide();
          $bttn_next1.show();
          $bttn_prev1.show();
          $mybookFood.show().booklet({
            name: null, //
            width: 800, //
            height: 500, //
            speed: 600, //
            direction: "LTR", //
            //
            next: $bttn_next1, //
            prev: $bttn_prev1, //
          });
          Cufon.refresh();
        }
      })
      .attr("src", source);
  });
});

$(function () {
  var $mybookGovernment = $("#mybookGovernment");
  var $bttn_next = $("#next_page_button");
  var $bttn_prev = $("#prev_page_button");
  var $loading = $("#loading");
  var $mybookGovernment_images = $mybookGovernment.find("img");
  var cnt_images = $mybookGovernment_images.length;
  var loaded = 0;

  $mybookGovernment_images.each(function () {
    var $img = $(this);
    var source = $img.attr("src");
    $("<img/>")
      .load(function () {
        ++loaded;
        if (loaded == cnt_images) {
          $loading.hide();
          $bttn_next.show();
          $bttn_prev.show();
          $mybookGovernment.show().booklet({
            name: null, //
            width: 800, //
            height: 500, //
            speed: 600, //
            direction: "LTR", //
            //
            next: $bttn_next, //
            prev: $bttn_prev, //
          });
          Cufon.refresh();
        }
      })
      .attr("src", source);
  });
});

$(function () {
  var $mybookHR = $("#mybookHR");
  var $bttn_next = $("#next_page_button");
  var $bttn_prev = $("#prev_page_button");
  var $loading = $("#loading");
  var $mybookHR_images = $mybookHR.find("img");
  var cnt_images = $mybookHR_images.length;
  var loaded = 0;

  $mybookHR_images.each(function () {
    var $img = $(this);
    var source = $img.attr("src");
    $("<img/>")
      .load(function () {
        ++loaded;
        if (loaded == cnt_images) {
          $loading.hide();
          $bttn_next.show();
          $bttn_prev.show();
          $mybookHR.show().booklet({
            name: null, //
            width: 800, //
            height: 500, //
            speed: 600, //
            direction: "LTR", //
            //
            next: $bttn_next, //
            prev: $bttn_prev, //
          });
          Cufon.refresh();
        }
      })
      .attr("src", source);
  });
});

$(function () {
  var $mybookNgo = $("#mybookNgo");
  var $bttn_next1 = $("#next_page_button1");
  var $bttn_prev1 = $("#prev_page_button1");
  var $loading = $("#loading");
  var $mybookNgo_images = $mybookNgo.find("img");
  var cnt_images = $mybookNgo_images.length;
  var loaded = 0;

  $mybookNgo_images.each(function () {
    var $img = $(this);
    var source = $img.attr("src");
    $("<img/>")
      .load(function () {
        ++loaded;
        if (loaded == cnt_images) {
          $loading.hide();
          $bttn_next1.show();
          $bttn_prev1.show();
          $mybookNgo.show().booklet({
            name: null, //
            width: 800, //
            height: 500, //
            speed: 600, //
            direction: "LTR", //
            //
            next: $bttn_next1, //
            prev: $bttn_prev1, //
          });
          Cufon.refresh();
        }
      })
      .attr("src", source);
  });
});

$(function () {
  var $mybookBPO = $("#mybookBPO");
  var $bttn_next1 = $("#next_page_button1");
  var $bttn_prev1 = $("#prev_page_button1");
  var $loading = $("#loading");
  var $mybookBPO_images = $mybookBPO.find("img");
  var cnt_images = $mybookBPO_images.length;
  var loaded = 0;

  $mybookBPO_images.each(function () {
    var $img = $(this);
    var source = $img.attr("src");
    $("<img/>")
      .load(function () {
        ++loaded;
        if (loaded == cnt_images) {
          $loading.hide();
          $bttn_next1.show();
          $bttn_prev1.show();
          $mybookBPO.show().booklet({
            name: null, //
            width: 800, //
            height: 500, //
            speed: 600, //
            direction: "LTR", //
            //
            next: $bttn_next1, //
            prev: $bttn_prev1, //
          });
          Cufon.refresh();
        }
      })
      .attr("src", source);
  });
});

$(function () {
  var $mybookMem = $("#mybookMem");
  var $bttn_next1 = $("#next_page_button1");
  var $bttn_prev1 = $("#prev_page_button1");
  var $loading = $("#loading");
  var $mybookMem_images = $mybookMem.find("img");
  var cnt_images = $mybookMem_images.length;
  var loaded = 0;

  $mybookMem_images.each(function () {
    var $img = $(this);
    var source = $img.attr("src");
    $("<img/>")
      .load(function () {
        ++loaded;
        if (loaded == cnt_images) {
          $loading.hide();
          $bttn_next1.show();
          $bttn_prev1.show();
          $mybookMem.show().booklet({
            name: null, //
            width: 800, //
            height: 500, //
            speed: 600, //
            direction: "LTR", //
            //
            next: $bttn_next1, //
            prev: $bttn_prev1, //
          });
          Cufon.refresh();
        }
      })
      .attr("src", source);
  });
});

$(function () {
  var $mybookOthers = $("#mybookOthers");
  var $bttn_next1 = $("#next_page_button1");
  var $bttn_prev1 = $("#prev_page_button1");
  var $loading = $("#loading");
  var $mybookOthers_images = $mybookOthers.find("img");
  var cnt_images = $mybookOthers_images.length;
  var loaded = 0;

  $mybookOthers_images.each(function () {
    var $img = $(this);
    var source = $img.attr("src");
    $("<img/>")
      .load(function () {
        ++loaded;
        if (loaded == cnt_images) {
          $loading.hide();
          $bttn_next1.show();
          $bttn_prev1.show();
          $mybookOthers.show().booklet({
            name: null, //
            width: 800, //
            height: 500, //
            speed: 600, //
            direction: "LTR", //
            //
            next: $bttn_next1, //
            prev: $bttn_prev1, //
          });
          Cufon.refresh();
        }
      })
      .attr("src", source);
  });
});
