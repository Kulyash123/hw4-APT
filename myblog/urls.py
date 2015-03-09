from django.conf.urls import patterns, include, url
from django.contrib import admin

from post.api import Post, Comment

post_res = PostResource()
comment_res = CommentResource()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'myblog.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

  url(r'^admin/', include(admin.site.urls)),
  url(r'^api/', include(post_res.urls)),
  url(r'^api/', include(comment_res.urls)),.urls)),
)
