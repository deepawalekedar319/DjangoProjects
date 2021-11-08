from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class CustomManager(models.Manager):
	def get_queryset(self):
		return super().get_queryset().filter(status='published')

class Post(models.Model):
		STATUS_CHOICES = (('draft','Draft'),('published','Published'))
		sno = models.AutoField(primary_key=True)
		title = models.CharField(max_length = 256)
		slug = models.SlugField(max_length = 264,unique_for_date='publish')
		author = models.ForeignKey(User,related_name = 'blog_posts',on_delete = models.CASCADE)
		body = models.TextField()
		liked = models.ManyToManyField(User,default=None,blank=True,related_name='Liked')
		publish = models.DateTimeField(default = timezone.now)
		created = models.DateTimeField(auto_now_add = True)
		updated = models.DateTimeField(auto_now = True)
		status = models.CharField(max_length = 10,choices = STATUS_CHOICES ,default = 'draft')
		objects = CustomManager()
			
		class Meta:
			ordering = ('-publish',)

		def __str__(self):
			return self.title

		def get_absolute_url(self):
			return reverse('post_detail',args=[self.publish.year,self.publish.strftime('%m'),self.publish.strftime('%d'),self.slug])
		
		@property
		def num_likes(self):
			return self.liked.all().count()

class Comments(models.Model):
	sno = models.AutoField(primary_key=True)
	post=models.ForeignKey(Post,related_name='comments',on_delete=models.CASCADE)
	name=models.CharField(max_length=32)
	user = models.ForeignKey(User,related_name = 'blog_comments',on_delete = models.CASCADE)
	email=models.EmailField()
	body=models.TextField()
	parent=models.ForeignKey('self',on_delete=models.CASCADE,null=True)
	created=models.DateTimeField(auto_now_add=True)
	updated=models.DateTimeField(auto_now=True)
	active=models.BooleanField(default=True)
	reply = models.ForeignKey('Comments', on_delete=models.CASCADE, related_name='replies', null=True)

	class Meta:
		ordering=('-created',)

	def __str__(self):
		return 'Commented by {} on {}'.format(self.name,self.post)

	

LIKE_CHOICES = {
	('Like','Like'),
	('Unlike','Unlike'),
}

class Like(models.Model):
	user = models.ForeignKey(User,on_delete=models.CASCADE)
	post = models.ForeignKey(Post,on_delete=models.CASCADE)
	value = models.CharField(choices=LIKE_CHOICES,default='Like' ,max_length=10)

	def __str__(self):
		return str(self.post)


RATE_CHOICES = [
	(1, 'Trash'),
	(2, 'Horrible'),
	(3, 'Terrible'),
	(4, 'Bad'),
	(5, 'OK'),
	(6, 'Readable'),
	(7, 'Good'),
	(8, 'Very Good'),
	(9, 'Perfect'),
	(10, 'Master Piece'), 
]

class Review(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	post = models.ForeignKey(Post, on_delete=models.CASCADE)
	date = models.DateTimeField(auto_now_add=True)
	rate = models.PositiveSmallIntegerField(choices=RATE_CHOICES)

	def __str__(self):
		return str(self.rate)

