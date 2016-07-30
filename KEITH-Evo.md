---
layout: page
title: KEITH Evolution (2015)
---

This is an archive of the KEITH Evolution blog from 2015. Each title is a link to the post.

For information regarding our next PiWars entry, head over to the [blog]({{ site.blogurl }})!

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

<p>If you haven't already, don't forget to subscribe to our <a href="http://eepurl.com/bwu2Cj"><b>mailing list</b></a> or follow us on Twitter <a href="http://www.twitter.com/{{ site.twitter_username }}"><b>@{{ site.twitter_username }}</b></a> for updates on when new blog posts are live!</p>
</div>
