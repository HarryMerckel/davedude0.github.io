---
layout: page
title: KEITH 3 (2017)
---

This is an archive of the KEITH 3 blog from 2017. Each post has links to the next and previous posts!

For information regarding our upcoming PiWars 2021 entry, please head over to the [<b>main blog</b>]({{ site.blogurl }}).

[![KEITH 3 (2017)](http://keiththerobot.uk/images/IMG_0903.JPG "KEITH 3 (2017)")](http://keiththerobot.uk/images/IMG_0903.JPG)

<div class="posts">
   {% for post in site.categories.K2017 reversed %} {% comment %} Display posts in forward chronological order - no longer an active blog! {% endcomment %}
     <div>
        <h2 class="post-title">
           <a href="{{ post.url }}">
              {{ post.title }}
           </a>
        </h2>
        <span class="post-date">{{ post.date | date_to_string }}</span>
        {% comment %} {{ post.content }} {% endcomment %}
      </div>
   {% endfor %}

<p>Why not follow us on Twitter <a href="http://www.twitter.com/{{ site.twitter_username }}"><b>@{{ site.twitter_username }}</b></a> for updates!</p>
</div>
