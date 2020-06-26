from django import forms

from Blog.models import BlogPost

class CreateBlogPostForm(forms.ModelForm):

    class Meta:
        model = BlogPost
        if BlogPost.image:
            fields = ['title', 'body', 'image']
        else:
            fields = ['title','body']

class UpdateBlogPostForm(forms.ModelForm):

    class Meta:
        model= BlogPost
        fields = ['title', 'body', 'image']

    def save(self, commit=True):
        blog_post = self.instance
        blog_post.title = self.cleaned_data['title']
        blog_post.body = self.cleaned_data['body']

        if self.cleaned_data['image']:
            blog_post.image = self.cleaned_data['image']

        if commit:
            blog_post.save()
        return blog_post