ARN
===

An `Amazon Resource Name <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__
uniquely identifies a cloud resource. It is a colon-delimited path:
``arn:partition:service:region:account:resource``. **ARN** matches that structure.

The construction is the :meth:`~edify.RegexBuilder.string` literal ``arn:``, then the
partition, service, an optionally-empty region and account, and the resource. The
region and account are allowed to be empty because global services such as object
storage leave them blank.

Resource names
--------------

.. edify-playground::

   from edify.library import arn

   arn("arn:aws:s3:::my-bucket")                              # a global service
   arn("arn:aws:iam::123456789012:user/alice")                # no region
   arn("arn:aws:lambda:us-east-1:123456789012:function:my-fn")
   arn("arn:aws-cn:s3:::bucket")                              # a different partition

Every segment is required
-------------------------

The colons must be present even when the fields between them are empty:

.. edify-playground::

   from edify.library import arn

   arn("arn:aws:s3:::my-bucket")   # empty region and account
   arn("arn:aws:s3:my-bucket")     # too few segments
   arn("not-an-arn")               # no prefix
   arn("ARN:aws:s3:::b")           # the prefix is lowercase
   arn("")                         # empty

The resource segment is matched permissively because its format varies by service —
some use ``type/id``, others ``type:id``, others a bare name. Matching an ARN does
not mean the resource exists or that you may access it; that is an authorisation
question.
