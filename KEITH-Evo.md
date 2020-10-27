---
layout: page
title: KEITH Evolution (2015)
---

This is an archive of the KEITH Evolution blog from 2015. Each post has links to the next and previous posts!

For information regarding our upcoming PiWars entry (when we get started!), please head over to the [<b>main blog</b>]({{ site.blogurl }}).

[![KEITH Evolution (2015)](http://keiththerobot.uk/images/evo-arty.jpg "KEITH Evolution (2015)")](http://keiththerobot.uk/images/evo-arty.jpg)

<div class="posts">
   {% for post in site.categories.evo reversed %} {% comment %} Display posts in forward chronological order - no longer an active blog! {% endcomment %}
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
