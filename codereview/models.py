from django.db import models
from django.contrib.auth.models import User

REVIEW_STATUS_CHOICES = (
    ( 'draft', 'Draft' ),
    ( 'awaiting_comments', 'Awaiting comments' ),
    ( 'awaiting_review', 'Awaiting review' ),
    ( 'reviewing', 'Undergoing review' ),
    ( 'archived', 'Archived' ),
)

REVIEW_ASSIGNMENT_ROLES = (
    ( 'reviewee', 'Reviewee' ),
    ( 'reviewer', 'Reviewer' ),
    ( 'moderator', 'Moderator' ),
    ( 'observer', 'Observer' ),
)

# Create your models here.
class Review( models.Model ):
    title = models.CharField( max_length = 255 )
    created = models.DateTimeField( auto_now_add = True )
    modified = models.DateTimeField( auto_now = True )
    review_date = models.DateTimeField() 
    description = models.TextField()
    status = models.CharField( choices = REVIEW_STATUS_CHOICES, max_length = 20 )
    participants = models.ManyToManyField( User, through = 'Assignment' )
    
    def __str__( self ):
        return self.title


class Assignment( models.Model ):
    review = models.ForeignKey( Review )
    user = models.ForeignKey( User )
    role = models.CharField( choices = REVIEW_ASSIGNMENT_ROLES, max_length = 10 )
    
    def __str__( self ):
        return "%s <%s>" % ( user.username, role )


class File( models.Model ):
    review = models.ForeignKey( Review )
    created = models.DateTimeField( auto_now_add = True )
    title = models.CharField( max_length = 255 )
    description = models.TextField()
    file_data = models.TextField()
    mime_type = models.CharField( max_length = 255 )
    
    def __str__( self ):
        return self.title


class Comment( models.Model ):
    review_file = models.ForeignKey( File )
    created = models.DateTimeField( auto_now_add = True )
    author = models.ForeignKey( User )
    start_index = models.IntegerField()
    end_index = models.IntegerField()
    content = models.TextField()
        
    def __str__( self ):
        return self.content[:30]
    