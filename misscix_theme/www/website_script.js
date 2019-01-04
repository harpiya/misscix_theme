/**
 * @Author: Saadettin Yasir AKEL <developer>
 * @Date:   2019-01-04T22:15:49+03:00
 * @Email:  yasir@harpiya.com
 * @Project: Harpiya Kurumsal Yönetim Sistemi
 * @Filename: website_script.js
 * @Last modified by:   developer
 * @Last modified time: 2019-01-04T22:16:00+03:00
 * @License: MIT License. See license.txt
 * @Copyright: Harpiya Yazılım Teknolojileri
 */
 // website_script.js
 {% if javascript -%}{{ javascript }}{%- endif %}

 {% if google_analytics_id -%}
 // Google Analytics
 (function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){
 (i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),
 m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)
 })(window,document,'script','//www.google-analytics.com/analytics.js','ga');

 ga('create', '{{ google_analytics_id }}', 'auto');
 ga('send', 'pageview');
 // End Google Analytics
 {%- endif %}
