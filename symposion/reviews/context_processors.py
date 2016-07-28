from symposion.proposals.models import ProposalSection


def reviews(request):
    sections = {}
    #manager = []
    for section in ProposalSection.objects.select_related('section'):
        if request.user.has_perm("reviews.can_review_%s" % section.section.slug):
            sections[section] = False
            if request.user.has_perm("reviews.can_manage_%s" % section.section.slug):
                sections[section] = True
    #temp = zip(sections, manager)
    print 'hello'
    return {
        "review_sections": sections,
    }
