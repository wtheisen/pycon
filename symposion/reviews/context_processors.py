from symposion.proposals.models import ProposalSection


def reviews(request):
    sections = []
    for section in ProposalSection.objects.select_related('section'):
        if request.user.has_perm("reviews.can_review_%s" % section.section.slug):
            info = []
            info.append(section)
            if request.user.has_perm("reviews.can_manage_%s" % section.section.slug):
                info.append(True)
            else:
                info.append(False)
            sections.append(info)
    print sections
    return {
        "review_sections": sections,
    }
