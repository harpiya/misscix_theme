/**
 * @Author: Saadettin Yasir AKEL <developer>
 * @Date:   2019-01-07T13:38:15+03:00
 * @Email:  yasir@harpiya.com
 * @Project: Harpiya Kurumsal Yönetim Sistemi
 * @Filename: function-select-custom.js
 * @Last modified by:   developer
 * @Last modified time: 2019-01-07T22:26:38+03:00
 * @License: MIT License. See license.txt
 * @Copyright: Harpiya Yazılım Teknolojileri
 */



$(document).ready(function(){
    // --------custom select--------------
$('select').each(function(){
    var $this = $(this), numberOfOptions = $(this).children('option').length;

    $this.addClass('select-hidden');
    $this.wrap('<div class="select item-view-attribute"></div>');
    $this.after('<div class="select-styled item-view-attribute"></div>');

});
// -------end--------------------
});
