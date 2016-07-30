---
layout: page
title: KEITH Evolution (2015)
---

This is an archive of the KEITH Evolution blog from 2015. Each title is a link to the post.

For information regarding our next PiWars entry, head over to the [blog]({{ site.blogurl }})!

<div class="posts">
   {% for post in site.posts reversed %} {% comment %} Display posts in forward chronological order - no longer an active blog! {% endcomment %}
      {% comment %} Check that the post is meant to be displayed {% endcomment %}
      {% assign sticky = false %}
      {% assign hidden = false %}
      {% assign evo = false %}
      {% for cat in post.categories %} {% comment %} Check all categories - a bit cumbersome, might look into shortening {% endcomment %}
         {% if cat == 'sticky' %}
            {% assign sticky = true %}
         {% endif %}
         {% if cat == 'hidden' %}
            {% assign hidden = true %}
         {% endif %}
         {% if cat == 'evo' %}
            {% assign evo = true %}
         {% endif %}
      {% endfor %}
      {% if evo %} {% comment %} Only show the article if it is meant to be part of the KEITH Evolution page {% endcomment %}
         {% unless hidden %} {% comment %} Also only shows if article is not hidden {% endcomment %}
            {% unless sticky %} {% comment %} Only show the article if it is not sticky {% endcomment %}
               <div class="post">
                  <h3 class="post-title">
                     <a href="{{ post.url }}">
                        {{ post.title }}
                     </a>
                  </h3>
                  <span class="post-date">{{ post.date | date_to_string }}</span>
                  {% comment %} {{ post.content }} {% endcomment %}
                  </div>
               {% endunless %}
         {% endunless %}
      {% endif %}
   {% endfor %}
</div>

<p>If you haven't already, don't forget to subscribe to our <a href="http://eepurl.com/bwu2Cj"><b>mailing list</b></a> or follow us on Twitter @[{{ site.twitter_username }}](http://www.twitter.com/{{ site.twitter_username }}) for updates on when new blog posts are live!</p>

{% comment %}
<div class="pagination">
  {% if paginator.next_page %}
    <a class="pagination-item older" href="{{ site.evourl }}page{{paginator.next_page}}">Older</a>
  {% else %}
    <span class="pagination-item older">Older</span>
  {% endif %}
  {% if paginator.previous_page %}
    {% if paginator.page == 2 %}
      <a class="pagination-item newer" href="{{ site.evourl }}">Newer</a>
    {% else %}
      <a class="pagination-item newer" href="{{ site.evourl }}page{{paginator.previous_page}}">Newer</a>
    {% endif %}
  {% else %}
    <span class="pagination-item newer">Newer</span>
  {% endif %}
</div> {% endcomment %}
